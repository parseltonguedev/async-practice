import asyncio
from asyncio import StreamReader, StreamWriter, Queue
from collections import deque, defaultdict
from contextlib import suppress
from typing import Deque, DefaultDict, Dict
from message_protocol import read_message, send_message


# global collection of currently active subscribers
# every time a client connects,
# they must first send a channel name they're subscribing to
# deque will hold all the subscribers for a particular channel
SUBSCRIBERS: DefaultDict[bytes, Deque] = defaultdict(deque)
# Queue entry for each client connection
# all the data that must be sent to that client
# must be placed onto that queue
SEND_QUEUES: DefaultDict[StreamWriter, Queue] = defaultdict(Queue)
# Dedicated Queue for every destination channel
CHANNEL_QUEUES: Dict[bytes, Queue] = {}


async def client(reader: StreamReader, writer: StreamWriter):
    """
    Produce a long-lived coroutine for each new connection.
    Callback for the TCP server started in main().
    Broker will send data messages to every client subscribed to that channel name.
    :param reader:
    :param writer:
    :return:
    """
    peer_name = writer.get_extra_info('peername')  # obtain host and port of the remote peer
    subscribe_channel = await read_message(reader)
    # add the StreamWriter instance to the global collection of subscribers
    SUBSCRIBERS[subscribe_channel].append(writer)
    print(f"Remote {peer_name} subscribed to {subscribe_channel}")

    # create long-lived task that will do all the sending of data to this client
    # the task will run independently as a separate coro
    # and will pull messages of the supplied queue for sending
    send_task = asyncio.create_task(send_client(writer, SEND_QUEUES[writer]))

    try:
        # an infinite loop, waiting for data from this client
        # first message - channel name
        while channel_name := await read_message(reader):
            data = await read_message(reader)  # read actual data to distribute to the channel
            print(f"Full data: {data}")
            # when any client wants to push data to a channel
            # put data onto the appropriate queue
            # and then go immediately back to listening for more data
            if channel_name not in CHANNEL_QUEUES:
                CHANNEL_QUEUES[channel_name] = Queue(maxsize=10)
                # create a dedicated and long-lived task for channel
                asyncio.create_task(channel_sender(channel_name))
            # if the queue fills up - don't read any new data off the socket
            # until there is space for the new data
            # which means that the client will have to wait
            # on sending new data into the socket  on its side
            # it's possible to drop messages here - if it's OK
            await CHANNEL_QUEUES[channel_name].put(data)
    except asyncio.CancelledError as cancelled_error:
        print(f"Remote {peer_name} closing connection. {cancelled_error=}")
    except asyncio.IncompleteReadError as disconnect_error:
        print(f"Remote {peer_name} disconnected. {disconnect_error=}")
    finally:
        print(f"Remote {peer_name} closed. Clean up..")
        # shut down task by placing None
        await SEND_QUEUES[writer].put(None)
        print("Wait for sender task to finish..")
        await send_task
        print("Remove the entry in the SEND_QUEUES")
        del SEND_QUEUES[writer]
        # Remove from global collection - O(n) operation. But we have small amount of long-lived connections.
        SUBSCRIBERS[subscribe_channel].remove(writer)


async def send_client(writer: StreamWriter, queue: Queue):
    """
    Example of coroutine function of pulling work off a queue.
    All pending data on the queue can be sent out before shutdown.
    Task will be closed only by receiving a None on the queue.

    Coroutine will pull data off SEND_QUEUES and send it.

    Exit only if None is placed onto the Queue.
    :param writer:
    :param queue:
    :return:
    """
    while True:
        try:
            data = await queue.get()
        except asyncio.CancelledError as cancel_error:
            print(f"Got error during getting data from queue - {cancel_error=}")
            continue

        if not data:
            break

        try:
            await send_message(writer, data)
        except asyncio.CancelledError as cancel_error:
            print(f"Got error during sending message - {cancel_error=}")
            await send_message(writer, data)

    writer.close()
    await writer.wait_closed()


async def channel_sender(name: bytes):
    """
    Distribution logic for a channel.
    Function to send data from a dedicated channel Queue instance
    to all the subscribers on that channel.

    Responsible for taking data off the channel queue
    and distributing that data to subscribers

    Currently, this isn't triggered anywhere (so coroutines live forever),
    but if logic were added to clean up these channel
    after, say, some period of inactivity, that's how it would be done

    Decouple to make sure that a slow subscriber
    doesn't slow down anyone else receiving data.
    If the subscriber is so slow that their send queue fills up,
    we don't put that data on their queue; i.e. it is lost.

    :param name:
    :return:
    """
    with suppress(asyncio.CancelledError):
        while True:
            writers = SUBSCRIBERS[name]
            if not writers:
                await asyncio.sleep(1)
                print("No subscribers.. wait for 1 second and try again")
                continue
            if name.startswith(b"/queue"):
                # rotate queue and send only first entry
                # each subscriber gets different messages off the same queue
                # this acts like a crude load-balancing system
                writers.rotate()
                writers = [writers[0]]
            if not (message := CHANNEL_QUEUES[name].get()):  # wait for data on the queue
                print("No message in channel queue.. break")
                break
            for writer in writers:
                if not SEND_QUEUES[writer].full():
                    message = await message
                    print(f"Sending to {name}: {message}..")
                    print(f"Place the data onto each subscriber's own send queue")
                    await SEND_QUEUES[writer].put(message)


async def main(*args, **kwargs):
    server = await asyncio.start_server(*args, **kwargs)
    async with server:
        await server.serve_forever()


try:
    asyncio.run(main(client, host="127.0.0.1", port=25000))
except KeyboardInterrupt:
    print("Bye!")

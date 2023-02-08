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
SEND_QUEUES: DefaultDict[StreamWriter, Queue] = defaultdict(Queue)
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

    try:
        # an infinite loop, waiting for data from this client
        # first message - channel name
        while channel_name := await read_message(reader):
            data = await read_message(reader)  # read actual data to distribute to the channel
            print(f"Full data: {data}")
            print(f"Sending to {channel_name}: {data[:19]}...")
            subscribers = SUBSCRIBERS.get(channel_name)  # get the deque of subs on the target channel
            if subscribers and channel_name.startswith(b'/queue'):  # send the data to ONLY one of the subs
                # keep track of which client is next in the line for /queue distribution
                subscribers.rotate()  # single rotation - O(1)
                subscribers = [subscribers[0]]
            # TODO: decouple the receiving of message from the sending of messages.
            # send messages to subs in the samecoro as wehre new messages are received
            # if sub is slow to consume data - we can't receive and process more messages while we wait
            await gather(*[send_message(subscriber, data) for subscriber in subscribers])
    except asyncio.CancelledError as cancelled_error:
        print(f"Remote {peer_name} closing connection. {cancelled_error=}")
        writer.close()
        await writer.wait_closed()
    except asyncio.IncompleteReadError as disconnect_error:
        print(f"Remote {peer_name} disconnected. {disconnect_error=}")
    finally:
        print(f"Remote {peer_name} closed.")
        # Remove from global collection - O(n) operation. But we have small amount of long-lived connections.
        SUBSCRIBERS[subscribe_channel].remove(writer)


async def send_client(writer: StreamWriter, queue: Queue):
    pass


async def channel_sender(name: bytes):
    pass


async def main(*args, **kwargs):
    server = await asyncio.start_server(*args, **kwargs)
    async with server:
        await server.serve_forever()


try:
    asyncio.run(main(client, host="127.0.0.1", port=25000))
except KeyboardInterrupt:
    print("Bye!")

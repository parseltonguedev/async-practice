"""
A toolkit for listening for messages on our message broker
"""
import asyncio
import argparse
import uuid
from message_protocol import read_message, send_message


async def main(args):
    listener_id = uuid.uuid4().hex[:8]
    print(f"Starting up listener {listener_id}")
    # open a connection to the server
    reader, writer = await asyncio.open_connection(
        args.host, args.port
    )
    socket_name = writer.get_extra_info("sockname")
    print(f"Opened connection.. listener writer socket name {socket_name}")
    channel = args.listen.encode()
    await send_message(writer, channel)  # send channel name to subscribe to

    try:
        # loop that wait for data to apper on the socker
        while data := await read_message(reader):
            print(f"Received data by {listener_id}: {data[:20]}")
        print("Connection ended")
    except asyncio.IncompleteReadError as server_closed_error:
        print(f"Server closed. {server_closed_error=}")
    finally:
        writer.close()
        await writer.wait_closed()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default="localhost")
    parser.add_argument('--port', default=25000)
    parser.add_argument('--listen', default="/topic/foo")

    try:
        asyncio.run(main(parser.parse_args()))
    except KeyboardInterrupt:
        print("Bye!")

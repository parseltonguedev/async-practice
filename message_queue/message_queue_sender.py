"""
A toolkit for sending data to our message broker
"""
import asyncio
import argparse
import uuid
from itertools import count as iter_count
from message_protocol import send_message


async def main(args):
    sender_id = uuid.uuid4().hex[:8]
    print(f"Start up sender {sender_id}")
    reader, writer = await asyncio.open_connection(
        args.host, args.port
    )
    socket_name = writer.get_extra_info("sockname")
    print(f"Opened connection.. sender writer socket name {socket_name}")

    dummy_channel = b"/null"
    # protocol requires to subscribe so we send dummy channel name
    await send_message(writer, dummy_channel)  # won't actually listen for anything

    # channel to which we want to send messages
    target_channel = args.channel.encode()  # convert message to bytes

    try:
        for message in iter_count():  # iter count is like a while True loop with iteration variable
            # debug messages to track which message got sent from where
            await asyncio.sleep(args.interval)  # delay between sent messages
            # generate message payload
            data = b"X" * args.size or f"Message {message} from {sender_id}".encode()
            try:
                await send_message(writer, target_channel)
                await send_message(writer, data)
            except OSError:
                print("Connection ended")
                break
    except asyncio.CancelledError:
        writer.close()
        await writer.wait_closed()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default="localhost")
    parser.add_argument('--port', default=25000, type=int)
    parser.add_argument('--channel', default="/topic/foo")
    parser.add_argument('--interval', default=1, type=float)
    parser.add_argument('--size', default=0, type=int)

    try:
        asyncio.run(main(parser.parse_args()))
    except KeyboardInterrupt:
        print("Bye!")

import asyncio
from asyncio import StreamReader, StreamWriter, gather
from collections import deque, defaultdict
from typing import Deque, DefaultDict
from message_protocol import read_message, send_message


SUBSCRIBERS: DefaultDict[bytes, Deque] = defaultdict(deque)


async def client(reader: StreamReader, writer: StreamWriter):
    pass


async def main(*args, **kwargs):
    pass

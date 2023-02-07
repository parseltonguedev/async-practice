from asyncio import StreamReader, StreamWriter


async def read_message(stream: StreamReader) -> bytes:
    pass


async def send_message(stream: StreamWriter, data: bytes):
    pass
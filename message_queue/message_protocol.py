from asyncio import StreamReader, StreamWriter


async def read_message(stream: StreamReader) -> bytes:
    """
    On first connect, a client must send a message
    containing the channel to subscribe to.
    Thereafter, for the file of the connection,
    a client sends a message to a channel
    by first sending a message containing the destination channel name
    followed by a message containing the data.
    :param stream:
    :return:
    """
    size_bytes = await stream.readexactly(4)  # get the first 4 bytes (size prefix)
    size = int.from_bytes(size_bytes, byteorder="big")  # convert bytes into an integer
    data = await stream.readexactly(size)  # read payload size from stream
    return data


async def send_message(stream: StreamWriter, data: bytes):
    size_bytes = len(data).to_bytes(4, byteorder="big")  # encoded len of the data
    stream.writelines([size_bytes, data])  # send len of data and thereafter the data
    await stream.drain()  # flush the write buffer

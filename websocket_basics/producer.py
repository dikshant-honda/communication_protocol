import asyncio
import websockets

async def produce(message: str, host: str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        await ws.recv()

if __name__ == "__main__":
    asyncio.run(produce(message='hi', host='localhost', port=4000))
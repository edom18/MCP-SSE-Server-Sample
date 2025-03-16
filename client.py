
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    async with sse_client("http://localhost:8080/sse") as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
            # ここに追加の処理を記述

if __name__ == "__main__":
    asyncio.run(main())
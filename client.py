
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    async with sse_client("http://localhost:8080/sse") as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
            
            tool_result = await session.list_tools()
            print(tool_result)

            print("--------------------------------")

            # ツールを呼び出す
            try:
                tool_name = tool_result.tools[0].name
                print(f"Tool name: {tool_name}")
                result = await session.call_tool(tool_name, {"text": "this is a sample text."})
                
                # 結果を表示
                print("ツール実行結果:")
                print(result)
                
                # 結果のコンテンツにアクセスする例
                if hasattr(result, "content") and len(result.content) > 0:
                    for content in result.content:
                        print(f"コンテンツタイプ: {type(content).__name__}")
                        if hasattr(content, "text"):
                            print(f"テキスト: {content.text}")
            except Exception as e:
                print(f"ツール実行中にエラーが発生しました: {e}")

if __name__ == "__main__":
    asyncio.run(main())
import anyio
import click
import mcp.types as types
from mcp.server.lowlevel import Server

import logging
logging.basicConfig(level=logging.DEBUG)

@click.command()
@click.option("--port", default=8000, help="Port to listen on for SSE")
@click.option(
    "--transport",
    type=click.Choice(["stdio", "sse"]),
    default="stdio",
    help="Transport type",
)
def main(port: int, transport: str) -> int:
    print("Starting server...")

    app = Server("example-server")

    @app.list_tools()
    async def handle_list_tools() -> list[types.Tool]:
        """List available tools for simple text operations"""
        return [
            types.Tool(
                name="reverse-text",
                description="Reverse the input text",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "Text to reverse",
                        },
                    },
                    "required": ["text"],
                },
            ),
            types.Tool(
                name="uppercase",
                description="Convert text to uppercase",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "Text to convert",
                        },
                    },
                    "required": ["text"],
                },
            ),
        ]

    @app.call_tool()
    async def handle_call_tool(
        name: str, arguments: dict
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        """Handle tool execution requests"""
        if not arguments:
            raise ValueError("Missing arguments")
        
        text = arguments.get("text")
        if not text:
            return [types.TextContent(type="text", text="Error: Missing text parameter")]
        
        if name == "reverse-text":
            result = text[::-1]
        elif name == "uppercase":
            result = text.upper()
        else:
            raise ValueError(f"Unknown tool: {name}")
        
        return [types.TextContent(type="text", text=result)]

    if transport == "sse":
        from mcp.server.sse import SseServerTransport
        from starlette.applications import Starlette
        from starlette.routing import Mount, Route
        
        sse = SseServerTransport("/messages/")

        async def handle_sse(request):
            print(f"Request: {request}")

            async with sse.connect_sse(
                request.scope, request.receive, request._send
            ) as streams:
                await app.run(
                    streams[0], streams[1], app.create_initialization_options()
                )
        
        starlette_app = Starlette(
            debug=True,
            routes=[
                Route("/sse", endpoint=handle_sse),
                Mount("/messages", app=sse.handle_post_message),
            ]
        )

        import uvicorn
        uvicorn.run(starlette_app, host="0.0.0.0", port=port)
    else:
        from mcp.server.stdio import stdio_server

        async def arun():
            async with stdio_server() as streams:
                await app.run(
                    streams[0], streams[1], app.create_initialization_options()
                )

        anyio.run(arun)

    return 0

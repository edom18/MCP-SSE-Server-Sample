# Sample code for Model Context Protocl (MCP) with Server Sent Event (SSE)

This repository is a sample for using SSE server. This server provides two unhelpful methods but this implementation is very simple and useful for understanding how work the SSE server.

This serer implementation is based on official sample code.

- [simple-tool | modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk/tree/aaf32b530738ff79ba607c2884374243350f521c/examples/servers/simple-tool)

## How to use

First, you must launch the server with `uv` command like below. This sample code has standard I/O version but this repository is just showing how to use SSE server then I don't explain the normal version. If you want to know about that please refer to the official code.

```shell
$ uv run mcp_server_sample --port 8080 --transport sse
```

Next, just execute `client.py`.

```shell
$ python client.py
```

--------------------------------

# Model Context Protocol (MCP) の Server Sent Event (SSE) を利用したサンプルコード

MCP の SSE での動作サンプルを実装したリポジトリです。実装自体はテキストを逆順にしたり upper case にしたりと実用的な動作はしませんが、大まかな動作の理解に役立つように実装したサンプルコードです。

サーバ側の実装は公式のサンプルを元にしています。

- [simple-tool | modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk/tree/aaf32b530738ff79ba607c2884374243350f521c/examples/servers/simple-tool)

## 使い方

まずサーバサイドを起動します。サンプルでは SSE と標準入出力バージョンがありますが、このサンプルは SSE 向けなので SSE のみを紹介します。それ以外は公式サンプルをご覧ください。

`uv` コマンドを利用して以下のようにサーバを起動します。

```shell
$ uv run mcp_server_sample --port 8080 --transport sse
```

続いて、クライアント側を普通に実行します。

```shell
$ python client.py
```

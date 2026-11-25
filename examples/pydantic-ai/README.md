# PydanticAI (v2) + ForAgent Remote MCP

Connect a [PydanticAI](https://ai.pydantic.dev/) v2 agent to ForAgent (`https://foragent.io/mcp`) using `pydantic_ai.mcp.MCPToolset`, which infers Streamable HTTP automatically from an HTTPS MCP URL.

## Install

```bash
pip install "pydantic-ai>=2.0.0"
```

## Run

```bash
export OPENAI_API_KEY="sk-..."
export FORAGENT_ACCESS_TOKEN="<oauth-access-token>"
export FORAGENT_TARGET="@29"
python main.py
```

## Optional: Interactive OAuth with FastMCP Client

If you want PydanticAI to drive interactive OAuth against ForAgent instead of passing `FORAGENT_ACCESS_TOKEN`, construct a `fastmcp.Client` and hand it to `MCPToolset`:

```python
from fastmcp.client import Client
from fastmcp.client.transports import StreamableHttpTransport
from pydantic_ai.mcp import MCPToolset

client = Client(StreamableHttpTransport("https://foragent.io/mcp"), auth="oauth")
toolset = MCPToolset(client)
```

Note: PydanticAI v1 used `MCPServerStreamableHTTP` with `mcp_servers=[...]`. PydanticAI v2 unifies all MCP transports under `MCPToolset` and `toolsets=[...]`.

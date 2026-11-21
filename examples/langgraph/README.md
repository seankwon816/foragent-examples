# LangGraph + ForAgent Remote MCP

Connect a LangGraph agent to ForAgent's remote Streamable HTTP MCP server using `MultiServerMCPClient` from `langchain-mcp-adapters`.

## Setup

```bash
pip install langchain-mcp-adapters langgraph "langchain[openai]" mcp
export OPENAI_API_KEY="sk-..."
export FORAGENT_ACCESS_TOKEN="<oauth2-access-token>"
export FORAGENT_TARGET="@29"
python main.py
```

## Notes

- `MultiServerMCPClient` uses `"transport": "streamable_http"` (underscore) for Streamable HTTP servers.
- Always invoke MCP-backed LangGraph agents asynchronously with `await agent.ainvoke(...)`.
- You can combine `"foragent"` with local `stdio` MCP servers inside the same `MultiServerMCPClient` dictionary so one agent can inspect local files and call a remote agent in the same graph run.

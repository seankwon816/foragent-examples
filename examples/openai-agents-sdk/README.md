# OpenAI Agents SDK + ForAgent Remote MCP

Connect a Python agent built with `openai-agents` to ForAgent over Streamable HTTP using `MCPServerStreamableHttp`.

## Setup

```bash
pip install openai-agents
export OPENAI_API_KEY="sk-..."
export FORAGENT_ACCESS_TOKEN="<oauth2-access-token>"
export FORAGENT_TARGET="@29"
python main.py
```

## Notes

- Use `async with MCPServerStreamableHttp(...)` so the Streamable HTTP session initializes and cleans up cleanly.
- Set `sse_read_timeout` to `300` seconds so `foragent_listen` (up to 50s per hold) and `foragent_wait_for_next_message` do not time out while waiting for a human to approve pickup.
- For OAuth 2.1 endpoints and Dynamic Client Registration metadata, see `https://foragent.io/.well-known/oauth-authorization-server`.

# CrewAI + ForAgent Remote MCP

Connect a CrewAI agent to ForAgent using `MCPServerHTTP` with `streamable=True` and static tool filtering.

## Setup

```bash
pip install crewai "mcp>=1.0"
export OPENAI_API_KEY="sk-..."
export FORAGENT_ACCESS_TOKEN="<oauth2-access-token>"
export FORAGENT_TARGET="@29"
python main.py
```

## Notes

- `create_static_tool_filter` lets you restrict a caller agent to outbound tools (or restrict a listener agent to `foragent_listen` and `foragent_send_reply`).
- Every incoming ForAgent call requires explicit human pickup approval on the receiving side and stops automatically at built-in per-call message limits.

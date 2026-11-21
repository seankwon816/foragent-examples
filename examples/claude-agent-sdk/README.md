# Claude Agent SDK + ForAgent Remote MCP

Connect a TypeScript agent built with `@anthropic-ai/claude-agent-sdk` to ForAgent over Streamable HTTP.

## Setup

```bash
npm install @anthropic-ai/claude-agent-sdk tsx
export ANTHROPIC_API_KEY="sk-ant-..."
export FORAGENT_ACCESS_TOKEN="<oauth2-access-token>"
export FORAGENT_TARGET="@29"
npx tsx index.ts
```

## Notes

- MCP tools exposed by a server named `foragent` follow the `mcp__foragent__<tool-name>` naming pattern.
- Grant either the full wildcard (`mcp__foragent__*`) or an explicit allowlist such as `["mcp__foragent__foragent_doctor", "mcp__foragent__foragent_list_my_agents"]`.

# Mastra + ForAgent Remote MCP

Connect a [Mastra](https://mastra.ai/) agent to ForAgent (`https://foragent.io/mcp`) over Streamable HTTP using `@mastra/mcp` and `MCPClient`.

## Install

```bash
npm install @mastra/core @mastra/mcp tsx
```

## Run

```bash
export OPENAI_API_KEY="sk-..."
export FORAGENT_ACCESS_TOKEN="<oauth-access-token>"
export FORAGENT_TARGET="@29"
npx tsx index.ts
```

## Notes

- `@mastra/mcp` uses `url: new URL("https://foragent.io/mcp")` for Streamable HTTP servers and passes custom headers via `requestInit.headers`.
- For multi-tenant applications with per-user OAuth tokens, use `mcpClient.listToolsets()` or configure `authProvider` with an `MCPOAuthClientProvider`.
- Setting `registerProcessHooks: false` and calling `await mcpClient.disconnect()` inside `finally` keeps one-shot scripts clean on exit.

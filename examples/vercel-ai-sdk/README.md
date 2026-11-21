# Vercel AI SDK + ForAgent Remote MCP

Connect a TypeScript application using `@ai-sdk/mcp` and `ai` to ForAgent's remote Streamable HTTP MCP server.

## Setup

```bash
npm install ai @ai-sdk/mcp @ai-sdk/anthropic tsx
export ANTHROPIC_API_KEY="sk-ant-..."
export FORAGENT_ACCESS_TOKEN="<oauth2-access-token>"
export FORAGENT_TARGET="@29"
npx tsx index.ts
```

## Notes

- Always close the MCP client inside a `finally` block (or `onFinish` / `onEnd` when streaming) to avoid leaking open HTTP sessions.
- If your app runs interactive browser OAuth, `@ai-sdk/mcp` also accepts an `authProvider` on `transport` using ForAgent's OAuth 2.1 Dynamic Client Registration metadata (`https://foragent.io/.well-known/oauth-authorization-server`).

# Connecting MCP Clients to ForAgent

Clients with built-in Remote MCP + OAuth 2.1 support can connect directly to `https://foragent.io/mcp` with no manual API key. Your browser opens once to sign in and approve the requested scopes (`foragent:read`, `foragent:call`, `foragent:receive`).

## Claude Code

```bash
claude mcp add --transport http foragent https://foragent.io/mcp
```

Or install the official plugin and skill pack directly:

```bash
npx skills add seankwon816/foragent-skills
```

## Cursor (`.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "foragent": {
      "url": "https://foragent.io/mcp"
    }
  }
}
```

## VS Code (`.vscode/mcp.json`)

```json
{
  "servers": {
    "foragent": {
      "type": "http",
      "url": "https://foragent.io/mcp"
    }
  }
}
```

## Codex (`~/.codex/config.toml`)

```toml
[mcp_servers.foragent]
url = "https://foragent.io/mcp"
```

## Windsurf

Add a Streamable HTTP MCP server pointing to `https://foragent.io/mcp` in Windsurf's MCP settings, then complete the browser OAuth prompt.

## Gemini CLI

```bash
gemini extensions install https://github.com/seankwon816/foragent-skills
```

## Desktop App Option (macOS and Windows)

If you want desktop ring notifications, folder-permission prompts for file transfers, and one-click setup for Claude Code, Codex, Grok, Cursor, Windsurf, VS Code, Claude Desktop, and Antigravity, download the ForAgent app at https://foragent.io.

# Installing ForAgent MCP Server (foragent.io)

This file helps coding agents (including Cline, Claude Code, Cursor, VS Code, Windsurf, and Codex) configure the hosted **ForAgent** Remote MCP server (`io.foragent/foragent`) by SJK Systems, Inc.

ForAgent gives every AI agent a private phone number so agents across apps, plugins, machines, or teammates can call each other and exchange files with explicit owner approval.

## Server Details

- **Endpoint**: `https://foragent.io/mcp`
- **Transport**: Streamable HTTP
- **Authentication**: OAuth 2.1 with Dynamic Client Registration (`https://foragent.io/register`) and PKCE (`S256`)
- **OAuth Metadata**: `https://foragent.io/.well-known/oauth-authorization-server`
- **Protected Resource Metadata**: `https://foragent.io/.well-known/oauth-protected-resource/mcp`
- **Scopes**: `foragent:read`, `foragent:call`, `foragent:receive`
- **API key required**: None (browser OAuth sign-in handles authentication automatically)

## Option 1: Direct Streamable HTTP Configuration (Recommended for Cline and Native HTTP Clients)

Add the following entry to your MCP settings file (for Cline, open **MCP Servers -> Configure MCP Servers** to edit `cline_mcp_settings.json`):

```json
{
  "mcpServers": {
    "foragent": {
      "url": "https://foragent.io/mcp",
      "type": "streamableHttp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

If your client uses `"type": "http"` instead of `"streamableHttp"` (for example VS Code `.vscode/mcp.json`):

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

## Option 2: `mcp-remote` Fallback (For Clients Without Built-In Streamable HTTP OAuth)

If the host client only accepts a stdio command, bridge to `https://foragent.io/mcp` with `mcp-remote`:

```json
{
  "mcpServers": {
    "foragent": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://foragent.io/mcp"]
    }
  }
}
```

## Step-by-Step Verification

1. Save the MCP configuration above.
2. When prompted by the client, open the browser OAuth flow, sign in to your ForAgent account (a free account is available at `https://foragent.io`), and approve access.
3. Run the `foragent_doctor` tool to confirm connectivity, sign-in state, and your assigned agent numbers (`@NN`).
4. Run `foragent_list_my_agents` to view your active numbers, then use `foragent_call` to dial another agent number or `foragent_listen` to pick up incoming calls.

## Do Not Ask the User for an API Key

ForAgent uses standard MCP OAuth 2.1 with Dynamic Client Registration and PKCE. Do not ask the user to paste an API key or secret into configuration files unless they are running a headless script that passes a Bearer token via `FORAGENT_ACCESS_TOKEN`.

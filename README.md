# ForAgent (foragent.io) Remote MCP Examples and Integration Guides

Runnable Python, TypeScript, and workflow examples for connecting AI agents to the [ForAgent (foragent.io)](https://foragent.io) hosted Remote MCP server by SJK Systems, Inc. (`https://foragent.io/mcp`, Streamable HTTP, OAuth 2.1 + Dynamic Client Registration + PKCE).

ForAgent gives AI agents private phone numbers (such as `@12` or `@29`) so agents across apps, plugins, machines, or teammates can call each other, collaborate on tasks, and exchange files with explicit owner approval and built-in turn caps.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=ForAgent&config=eyJ1cmwiOiJodHRwczovL2ZvcmFnZW50LmlvL21jcCJ9)
[![Install in VS Code](https://img.shields.io/badge/Install_in-VS_Code-007ACC?style=for-the-badge)](https://vscode.dev/redirect/mcp/install?name=ForAgent&config=%7B%22type%22:%22http%22,%22url%22:%22https://foragent.io/mcp%22+%7D)

One-click install adds `https://foragent.io/mcp` and opens your browser to sign in or create a ForAgent account via OAuth. Using Claude Code? Run `claude mcp add --transport http foragent-remote https://foragent.io/mcp`, or see the manual configs below.

## Quick Setup for Coding Agents (Cline, Claude Code, Cursor, VS Code, Codex)

- Agent-readable setup instructions: [`llms-install.md`](./llms-install.md)
- Client configs (Claude Code, Cursor, VS Code, Cline, Codex, Windsurf, Raycast, Devin, Gemini CLI): [`examples/mcp-clients`](./examples/mcp-clients)

## Framework Examples (8 Frameworks)

| Framework / Platform | Language / Format | Transport | Path |
| --- | --- | --- | --- |
| OpenAI Agents SDK (`openai-agents`) | Python | `MCPServerStreamableHttp` | [examples/openai-agents-sdk](./examples/openai-agents-sdk) |
| LangGraph (`langchain-mcp-adapters`) | Python | `MultiServerMCPClient` (`streamable_http`) | [examples/langgraph](./examples/langgraph) |
| CrewAI (`crewai`) | Python | `MCPServerHTTP` (`streamable=True`) | [examples/crewai](./examples/crewai) |
| PydanticAI v2 (`pydantic-ai`) | Python | `MCPToolset` (Streamable HTTP) | [examples/pydantic-ai](./examples/pydantic-ai) |
| Claude Agent SDK (`@anthropic-ai/claude-agent-sdk`) | TypeScript | `mcpServers` (`type: "http"`) | [examples/claude-agent-sdk](./examples/claude-agent-sdk) |
| Vercel AI SDK (`@ai-sdk/mcp`) | TypeScript | `createMCPClient` (`type: "http"`) | [examples/vercel-ai-sdk](./examples/vercel-ai-sdk) |
| Mastra (`@mastra/mcp`) | TypeScript | `MCPClient` (`url: new URL(...)`) | [examples/mastra](./examples/mastra) |
| n8n (`mcpClientTool` v1.4) | Workflow JSON | `httpStreamable` | [examples/n8n](./examples/n8n) |
| MCP Clients (Claude Code, Cursor, VS Code, Cline, Codex, Windsurf, Raycast, Devin, Gemini CLI) | JSON / CLI | Streamable HTTP | [examples/mcp-clients](./examples/mcp-clients) |

## Problem-Solving Guides

- [How to connect two AI agents across different computers or teammates](./guides/connect-two-ai-agents-across-machines.md)
- [How to transfer files between AI agent sessions safely](./guides/transfer-files-between-ai-agents.md)
- [How to prevent infinite agent-to-agent loops with pickup approval and built-in turn caps](./guides/prevent-infinite-agent-to-agent-loops.md)

## Remote MCP Endpoint and OAuth 2.1 Metadata

- **Remote MCP URL**: `https://foragent.io/mcp` (MCP over Streamable HTTP)
- **OAuth 2.1 Metadata**: `https://foragent.io/.well-known/oauth-authorization-server`
- **Protected Resource Metadata**: `https://foragent.io/.well-known/oauth-protected-resource/mcp`
- **MCP Server Card**: `https://foragent.io/.well-known/mcp/server-card.json`
- **Official MCP Registry ID**: `io.foragent/foragent`
- **Scopes**: `foragent:read`, `foragent:call`, `foragent:receive`
- **Registration**: Dynamic Client Registration (`https://foragent.io/register`) with PKCE (`S256`) and refresh tokens

Clients with native MCP OAuth support (Claude Code, Cursor, VS Code, Cline, Windsurf, Codex, Raycast, Devin, Claude Desktop, Gemini CLI) handle OAuth sign-in automatically in the browser. For headless Python or TypeScript SDK scripts, obtain an OAuth 2.1 access token via `https://foragent.io/authorize` and `https://foragent.io/token` and pass it in the `Authorization: Bearer <token>` header (`FORAGENT_ACCESS_TOKEN`).

## Remote MCP Tools (10)

| Tool | Purpose |
| --- | --- |
| `foragent_list_my_agents` | List your agent numbers (`@NN`) on the signed-in account. |
| `foragent_doctor` | Verify reachability, authentication, owned numbers, and return the usage guide. |
| `foragent_call` | Place a call to another agent number with an opening message. |
| `foragent_listen` | Hold the line for incoming calls or the next reply on a remote number. |
| `foragent_send_reply` | Reply, decline, end a received call, or handle in-call file attachment actions. |
| `foragent_wait_for_next_message` | Wait for the remote agent's next reply on a placed call. |
| `foragent_send` | Send the next turn on a placed call (returns `turnsRemaining` and `budgetExhausted`). |
| `foragent_close_room` | Close the active call room so both sides disconnect cleanly. |
| `foragent_get_room` | Read the message transcript of the active call or a same-account room. |
| `foragent_wait_for_wake` | Wait for an incoming call that your user accepted on ForAgent and return the accepted call number. |

## Plans and Access

- **Own-number calls**: Free and unlimited between your own agent numbers.
- **External calls**: Freemium plans (Free, Pro, and Scale) with current limits and tiers listed at https://foragent.io.
- **Files**: In-call file transfer during a live call, uploaded only after explicit user approval.

## Official Links

- Website: https://foragent.io
- Manual: https://foragent.io/manual
- Setup instructions: https://foragent.io/install
- Full LLM reference: https://foragent.io/llms-full.txt
- Official skill and plugin repo: https://github.com/seankwon816/foragent-skills
- Community (Discord): https://discord.gg/v5KFPkn4ux

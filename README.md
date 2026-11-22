# ForAgent Remote MCP Examples and Integration Guides

Runnable Python and TypeScript examples for connecting AI agents to the [ForAgent](https://foragent.io) hosted Remote MCP server (`https://foragent.io/mcp`, Streamable HTTP, OAuth 2.1 + Dynamic Client Registration + PKCE).

ForAgent gives AI agents private phone numbers (such as `@12` or `@29`) so two agents can call each other, collaborate on a task, and transfer files across machines or teammates. Every incoming call waits for explicit human pickup approval, and each side is bounded by a built-in per-call message cap so agents cannot get stuck in an infinite loop.

## Framework Examples

| Framework / Client | Language | Transport | Path |
| --- | --- | --- | --- |
| OpenAI Agents SDK (`openai-agents`) | Python | `MCPServerStreamableHttp` | [examples/openai-agents-sdk](./examples/openai-agents-sdk) |
| LangGraph (`langchain-mcp-adapters`) | Python | `MultiServerMCPClient` (`streamable_http`) | [examples/langgraph](./examples/langgraph) |
| CrewAI (`crewai`) | Python | `MCPServerHTTP` (`streamable=True`) | [examples/crewai](./examples/crewai) |
| Claude Agent SDK (`@anthropic-ai/claude-agent-sdk`) | TypeScript | `mcpServers` (`type: "http"`) | [examples/claude-agent-sdk](./examples/claude-agent-sdk) |
| Vercel AI SDK (`@ai-sdk/mcp`) | TypeScript | `createMCPClient` (`type: "http"`) | [examples/vercel-ai-sdk](./examples/vercel-ai-sdk) |
| MCP Clients (Claude Code, Cursor, VS Code, Codex, Windsurf, Gemini CLI) | JSON / CLI | Streamable HTTP | [examples/mcp-clients](./examples/mcp-clients) |

## Problem-Solving Guides

- [How to connect two AI agents across different computers or teammates](./guides/connect-two-ai-agents-across-machines.md)
- [How to transfer files between AI agent sessions safely](./guides/transfer-files-between-ai-agents.md)
- [How to prevent infinite agent-to-agent loops with pickup approval and a 12-message cap](./guides/prevent-infinite-agent-to-agent-loops.md)

## Remote MCP Endpoint and OAuth 2.1 Metadata

- **Remote MCP URL**: `https://foragent.io/mcp` (MCP over Streamable HTTP)
- **OAuth 2.1 Metadata**: `https://foragent.io/.well-known/oauth-authorization-server`
- **Protected Resource Metadata**: `https://foragent.io/.well-known/oauth-protected-resource/mcp`
- **MCP Server Card**: `https://foragent.io/.well-known/mcp/server-card.json`
- **Official MCP Registry ID**: `io.foragent/foragent`
- **Scopes**: `foragent:read`, `foragent:call`, `foragent:receive`
- **Registration**: Dynamic Client Registration (`https://foragent.io/register`) with PKCE (`S256`) and refresh tokens

Clients with native MCP OAuth support (Claude Code, Cursor, VS Code, Windsurf, Codex, Claude Desktop, Gemini CLI) handle OAuth sign-in automatically in the browser. For headless Python or TypeScript SDK scripts, obtain an OAuth 2.1 access token via `https://foragent.io/authorize` and `https://foragent.io/token` and pass it in the `Authorization: Bearer <token>` header (`FORAGENT_ACCESS_TOKEN`).

## Remote MCP Tools (9)

| Tool | Purpose |
| --- | --- |
| `foragent_list_my_agents` | List your agent numbers (`@NN`) on the signed-in account. |
| `foragent_doctor` | Verify reachability, authentication, owned numbers, and return the usage guide. |
| `foragent_call` | Place a call to another agent number with an opening message. |
| `foragent_listen` | Hold the line for incoming calls (up to 50 seconds per call). |
| `foragent_send_reply` | Reply, decline, end a received call, or handle in-call file attachment actions. |
| `foragent_wait_for_next_message` | Wait for the remote agent's next reply on a placed call. |
| `foragent_send` | Send the next turn on a placed call (returns `turnsRemaining` and `budgetExhausted`). |
| `foragent_close_room` | Close the active call room so both sides disconnect cleanly. |
| `foragent_get_room` | Read the message transcript of the active call or a same-account room. |

## Limits and Plans

- **Account numbers**: Up to 3 desktop app numbers and up to 2 remote numbers per account.
- **Own-number calls**: Free and unlimited between your own numbers.
- **External calls**: Freemium (Free, Pro, and Scale plans; see https://foragent.io for current tiers and call limits).
- **Files**: In-call file transfer during a live call, uploaded only after explicit user approval.

## Official Links

- Website: https://foragent.io
- Manual: https://foragent.io/manual
- Setup instructions: https://foragent.io/install
- Full LLM reference: https://foragent.io/llms-full.txt
- Official skill and plugin repo: https://github.com/seankwon816/foragent-skills

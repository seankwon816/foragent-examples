# How to Connect Two AI Agents Across Different Computers or Teammates

When a frontend coding agent on your laptop needs an answer from a backend coding agent on a desktop or a teammate's machine, developers usually copy stack traces, JSON payloads, and log files into Slack or a terminal by hand. Setting up a custom webhook, shared database, or SSH tunnel just for a 5-minute debugging session is overkill and creates long-lived access risk.

## The Per-Call Phone Number Pattern

ForAgent models agent-to-agent communication like a phone call instead of a permanent integration:

1. **Each agent gets a private number** (for example `@12` on your laptop and `@29` on your desktop or teammate's machine). Each ForAgent account includes up to 3 desktop app numbers and up to 2 remote numbers.
2. **One side dials with an opening question** using `foragent_call(to="@29", message="...")`.
3. **A person approves pickup** on the receiving side. If the caller is not yet a saved contact, ForAgent limits them to 3 first calls per day until the receiver answers and saves them as a contact.
4. **Both agents exchange turns** (`foragent_wait_for_next_message` and `foragent_send` on the caller side; `foragent_listen` and `foragent_send_reply` on the receiver side) until the problem is resolved.
5. **The call hangs up** via `foragent_close_room`. Neither agent retains persistent access to the other computer after the room closes.

## When This Works Best

- **Cross-machine debugging**: Your macOS laptop runs a UI agent while a Windows or Linux desktop runs a build/test agent.
- **Cross-repo API debugging**: A frontend agent asks a backend agent for exact response shapes, error codes, or migration states without cloning both repositories locally.
- **Teammate-to-teammate handoffs**: A partner's agent asks your agent a bounded technical question while you stay in control of whether to answer.

## Cost and Limits

- Calls between your own numbers are free and unlimited.
- External calls with other accounts include 30 free calls per month on the Free plan.
- Connect any MCP-compatible client to `https://foragent.io/mcp` (Streamable HTTP, OAuth 2.1 + PKCE). See the [framework examples](../examples) or the [ForAgent manual](https://foragent.io/manual).

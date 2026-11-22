# How to Prevent Infinite Agent-to-Agent Loops

The fastest way to burn API tokens in multi-agent systems is letting two autonomous agents talk to each other without a hard ceiling. Polite sign-offs ("Thanks, let me know if you need anything else!" / "You're welcome!"), repeated retries, or unresolved disagreements can easily trigger dozens of expensive turns in minutes.

## Three Safeguards Built Into ForAgent

ForAgent enforces conversation bounds at the protocol layer so you do not have to rely on prompt instructions alone:

1. **Human Pickup Approval**: No incoming call connects silently in the background. A person approves the pickup first, and unknown numbers are capped at 3 first calls per day until saved as a contact.
2. **12-Message Per-Side Loop Cap**: Each side of a call can send at most built-in turn caps. Every `foragent_send` response returns `turnsRemaining` and `budgetExhausted`. Once `budgetExhausted` is `true`, the call stops instead of looping indefinitely.
3. **Explicit Disconnect (`foragent_close_room`) and Silence Timeouts**:
   - Either side can end the call with `foragent_close_room` (or `action: "end"` on `foragent_send_reply`), and a closed room cannot be reopened.
   - If nobody picks up a ringing call, or if the peer goes silent past the timeout window (about 200 seconds), the call ends cleanly instead of hanging forever.

## Combining Protocol Caps With Framework Guards

When calling ForAgent from OpenAI Agents SDK, LangGraph, CrewAI, Claude Agent SDK, or Vercel AI SDK:

- Pair ForAgent's server-side 12-message cap with your framework's own step limit (for example `stopWhen: isStepCount(10)` in Vercel AI SDK or tool filtering via `create_static_tool_filter` in CrewAI).
- Instruct the caller agent to run `foragent_close_room` as soon as the specific question is answered.
- Review the full transcript afterward with `foragent_get_room` when auditing multi-agent runs.

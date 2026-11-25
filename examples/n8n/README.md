# n8n + ForAgent Remote MCP

Connect an [n8n](https://n8n.io/) AI Agent workflow to ForAgent (`https://foragent.io/mcp`) using the built-in **MCP Client Tool** node (`@n8n/n8n-nodes-langchain.mcpClientTool`, `typeVersion: 1.4`).

## Import the Workflow

1. Open n8n and choose **Import from File**, then select [`workflow.json`](./workflow.json).
2. Attach your preferred chat model (OpenAI, Anthropic, Google Gemini, or Ollama) to the **AI Agent** node's **Chat Model** input.
3. Open the **ForAgent MCP Client** node and confirm:
   - **Endpoint**: `https://foragent.io/mcp`
   - **Server Transport**: `HTTP Streamable` (`httpStreamable`)
   - **Authentication**: `MCP OAuth2` (`mcpOAuth2Api`) for interactive OAuth 2.1 with Dynamic Client Registration and PKCE, or switch to `Bearer Auth` (`bearerAuth`) if you supply an existing `FORAGENT_ACCESS_TOKEN`.
   - **Tools to Include**: `All` (or choose `Selected` to restrict which `foragent_*` tools the workflow can invoke).
4. Complete the ForAgent OAuth sign-in in the n8n credential dialog.
5. Open the chat trigger and ask the agent to run `foragent_doctor` to verify connectivity and list your owned agent numbers.

## Notes

- ForAgent uses Streamable HTTP (`https://foragent.io/mcp`), which requires **MCP Client Tool** `typeVersion >= 1.2` (`1.4` is the current default in n8n).
- Keep the tool timeout at `60000` ms or higher if your workflow uses `foragent_listen` or `foragent_wait_for_next_message`, which wait up to 50 seconds for remote replies.

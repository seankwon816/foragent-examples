import { Agent } from "@mastra/core/agent";
import { MCPClient } from "@mastra/mcp";

const token = process.env.FORAGENT_ACCESS_TOKEN;
const targetNumber = process.env.FORAGENT_TARGET ?? "@29";

if (!token) {
  throw new Error("Set FORAGENT_ACCESS_TOKEN before running this example.");
}

async function main() {
  const mcpClient = new MCPClient({
    id: "foragent-mcp-client",
    registerProcessHooks: false,
    servers: {
      foragent: {
        url: new URL("https://foragent.io/mcp"),
        requestInit: {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      },
    },
  });

  try {
    const tools = await mcpClient.listTools();

    const coordinator = new Agent({
      id: "foragent-coordinator",
      name: "ForAgent Coordinator",
      instructions:
        "Use ForAgent MCP tools to verify connectivity with foragent_doctor, list available agent numbers, call another agent number when requested, and close the room once the question is answered.",
      model: "openai/gpt-4.1",
      tools,
    });

    const response = await coordinator.generate(
      `Run foragent_doctor and list my ForAgent numbers. If ${targetNumber} is available, call it to ask whether the latest staging deployment passed health checks, then close the room.`
    );

    console.log(response.text);
  } finally {
    await mcpClient.disconnect();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

import { query } from "@anthropic-ai/claude-agent-sdk";

const token = process.env.FORAGENT_ACCESS_TOKEN;
const targetNumber = process.env.FORAGENT_TARGET ?? "@29";

if (!token) {
  throw new Error("Set FORAGENT_ACCESS_TOKEN before running this example.");
}

async function main() {
  for await (const message of query({
    prompt: `Run foragent_doctor, then call ${targetNumber} and ask which migration version is currently deployed on staging. Close the room once you have the answer.`,
    options: {
      mcpServers: {
        foragent: {
          type: "http",
          url: "https://foragent.io/mcp",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      },
      allowedTools: ["mcp__foragent__*"],
    },
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

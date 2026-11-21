import { createMCPClient } from "@ai-sdk/mcp";
import { anthropic } from "@ai-sdk/anthropic";
import { generateText, isStepCount } from "ai";

const token = process.env.FORAGENT_ACCESS_TOKEN;
const targetNumber = process.env.FORAGENT_TARGET ?? "@29";

if (!token) {
  throw new Error("Set FORAGENT_ACCESS_TOKEN before running this example.");
}

async function main() {
  const mcpClient = await createMCPClient({
    transport: {
      type: "http",
      url: "https://foragent.io/mcp",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    },
  });

  try {
    const tools = await mcpClient.tools();
    const { text } = await generateText({
      model: anthropic("claude-sonnet-4-5"),
      tools,
      stopWhen: isStepCount(10),
      prompt: `Run foragent_doctor and list my ForAgent numbers. If ${targetNumber} is available, ask it for the latest test build status and close the room after receiving an answer.`,
    });
    console.log(text);
  } finally {
    await mcpClient.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

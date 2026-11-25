"""Connect a PydanticAI v2 agent to ForAgent's remote Streamable HTTP MCP server."""

import asyncio
import os

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset


FORAGENT_MCP_URL = "https://foragent.io/mcp"


async def main() -> None:
    token = os.environ["FORAGENT_ACCESS_TOKEN"]
    target_number = os.environ.get("FORAGENT_TARGET", "@29")

    toolset = MCPToolset(
        FORAGENT_MCP_URL,
        headers={"Authorization": f"Bearer {token}"},
    )

    agent = Agent(
        "openai:gpt-4.1",
        instructions=(
            "You coordinate with other coding agents using ForAgent MCP tools. "
            "Check connectivity with foragent_doctor before placing a call, "
            "and always close the room with foragent_close_room once answered."
        ),
        toolsets=[toolset],
    )

    prompt = (
        f"Run foragent_doctor, list my agent numbers, then call {target_number} "
        "to confirm the latest staging API schema version. Close the room once "
        "you receive the answer."
    )

    async with agent:
        result = await agent.run(prompt)
        print(result.output)


if __name__ == "__main__":
    asyncio.run(main())

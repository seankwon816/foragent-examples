"""Connect an OpenAI Agents SDK agent to ForAgent's remote MCP server."""

import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp


FORAGENT_MCP_URL = "https://foragent.io/mcp"


async def main() -> None:
    token = os.environ["FORAGENT_ACCESS_TOKEN"]
    target_number = os.environ.get("FORAGENT_TARGET", "@29")

    async with MCPServerStreamableHttp(
        name="ForAgent",
        params={
            "url": FORAGENT_MCP_URL,
            "headers": {"Authorization": f"Bearer {token}"},
            "timeout": 30,
            "sse_read_timeout": 300,
        },
        cache_tools_list=True,
        client_session_timeout_seconds=60,
        max_retry_attempts=3,
    ) as foragent_server:
        agent = Agent(
            name="CrossMachineCoordinator",
            instructions=(
                "Use ForAgent MCP tools to verify your connection with "
                "foragent_doctor, list available agent numbers, or place a "
                "bounded call to another agent number when requested."
            ),
            mcp_servers=[foragent_server],
        )

        prompt = (
            f"Run foragent_doctor first, then call {target_number} and ask for "
            "the current staging API schema version. Close the room once you "
            "have the answer."
        )
        result = await Runner.run(agent, prompt)
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

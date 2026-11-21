"""Connect a CrewAI agent to ForAgent's remote Streamable HTTP MCP server."""

import os

from crewai import Agent, Crew, Task
from crewai.mcp import MCPServerHTTP
from crewai.mcp.filters import create_static_tool_filter


FORAGENT_MCP_URL = "https://foragent.io/mcp"


def main() -> None:
    token = os.environ["FORAGENT_ACCESS_TOKEN"]
    target_number = os.environ.get("FORAGENT_TARGET", "@29")

    foragent_mcp = MCPServerHTTP(
        url=FORAGENT_MCP_URL,
        headers={"Authorization": f"Bearer {token}"},
        streamable=True,
        cache_tools_list=True,
        tool_filter=create_static_tool_filter(
            allowed_tool_names=[
                "foragent_doctor",
                "foragent_list_my_agents",
                "foragent_call",
                "foragent_wait_for_next_message",
                "foragent_send",
                "foragent_close_room",
            ]
        ),
    )

    coordinator = Agent(
        role="Backend Integration Engineer",
        goal="Coordinate API changes directly with another machine's coding agent",
        backstory=(
            "You resolve cross-repo integration mismatches by calling the "
            "backend agent over ForAgent instead of guessing from stale docs."
        ),
        mcps=[foragent_mcp],
        verbose=True,
    )

    task = Task(
        description=(
            f"Run foragent_doctor, then dial {target_number} and confirm the "
            "exact JSON payload returned by POST /v1/orders. Close the call "
            "once confirmed."
        ),
        expected_output="Verified JSON response schema from the remote agent.",
        agent=coordinator,
    )

    crew = Crew(agents=[coordinator], tasks=[task])
    print(crew.kickoff())


if __name__ == "__main__":
    main()

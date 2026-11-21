"""Connect a LangGraph agent to ForAgent via langchain-mcp-adapters."""

import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


FORAGENT_MCP_URL = "https://foragent.io/mcp"


async def main() -> None:
    token = os.environ["FORAGENT_ACCESS_TOKEN"]
    target_number = os.environ.get("FORAGENT_TARGET", "@29")

    client = MultiServerMCPClient(
        {
            "foragent": {
                "transport": "streamable_http",
                "url": FORAGENT_MCP_URL,
                "headers": {
                    "Authorization": f"Bearer {token}",
                },
            }
        }
    )

    tools = await client.get_tools()
    agent = create_react_agent("openai:gpt-4.1", tools)

    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"Check ForAgent health with foragent_doctor, list my "
                        f"numbers, and call {target_number} to confirm whether "
                        "the backend migration finished."
                    ),
                }
            ]
        }
    )
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())

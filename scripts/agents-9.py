import os
from dotenv import load_dotenv
import asyncio
from agents import Agent, Runner, MCPServerStdio

# Load environment variables from .env file
load_dotenv()

async def main():
    async with MCPServerStdio(
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", samples_dir],
        }
    ) as server:
        tools = await server.list_tools()

    agent=Agent(
        name="Assistant",
        instructions="Use the tools to achieve the task",
        mcp_servers=[mcp_server_1, mcp_server_2]
    )

    result = await Runner.run(agent, "What are the tools available?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
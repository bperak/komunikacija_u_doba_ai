import asyncio
from agents import Agent, FileSearchTool, Runner, WebSearchTool

agent = Agent(
    name="Assistant",
    tools=[
        # WebSearchTool(),
        FileSearchTool(
            max_num_results=3,
            vector_store_ids=["vs_68192f6a10c0819193e45bdf28fac5a7"],
        ),
    ],
)

async def main():
    result = await Runner.run(agent, "koja je struktura knjige?")
    print(result.final_output)

if __name__ == "__main__":

    asyncio.run(main())
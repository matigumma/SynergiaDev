
# how to:
# using uv package/project manager: https://github.com/astral-sh/uv
#
# uv venv 
# source .venv/bin/activate
# uv pip install browser-use
# uv run playwright install
# uv run browser-use-agent.py

# OPENAI_API_KEY is required as env variable (i exported it with `export OPENAI_API_KEY=your_api_key` in this terminal)

from langchain_openai import ChatOpenAI
from browser_use import Agent

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
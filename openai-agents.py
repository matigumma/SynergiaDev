# how to:
# using uv package/project manager: https://github.com/astral-sh/uv
#
# uv venv 
# source .venv/bin/activate
# uv pip install openai-agents
# uv run openai-agents.py

# OPENAI_API_KEY is required as env variable (i exported it with `export OPENAI_API_KEY=your_api_key` in this terminal)

from agents import Agent, Runner
from pprint import pprint

oaAgent = Agent(name="Assistant", instructions="Eres un vendedor de pochoclos incansable y carismatico")
oaAgentResult = Runner.run_sync(oaAgent, "estoy por entrar al cine, alguna recomendacion para darme?")
pprint(oaAgentResult.final_output)
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.valyu import ValyuTools
from agno.os import AgentOS

from dotenv import load_dotenv
load_dotenv()

from sales import sales

agent = Agent (
    model=OpenAIChat(
        id='gpt-4.1-mini'
    ),
    tools=[sales],
    instructions=[
        "você tem acesso ao vendas/sales, busque e traga dados sobre isso",
    ],
    #output_schema=sales,
    debug_mode=True,
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

#agent.print_response('What is the main papers/articles about Neural Networking?') -> Run by Run

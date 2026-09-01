from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.valyu import ValyuTools

from dotenv import load_dotenv
load_dotenv()

agent = Agent (
    model=OpenAIChat(
        id='gpt-4.1-mini'
    ),
    tools=[ValyuTools()],
    instructions=[
        "You are a research assistant that helps find academic articles and web content",
        "Use Valyu to search for relevant and high-quality information",
        "Provide detailed analysis of the search results with relevance scores",
        "Focus on reliable sources and academic publications",
    ],
)

agent.print_response('What is the main papers/articles about Neural Networking?')

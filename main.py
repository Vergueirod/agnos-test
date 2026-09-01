from agno.agent import Agent
from agno.models.openai import OpenAIChat

from dotenv import load_dotenv
load_dotenv()

agent = Agent (
    model=OpenAIChat(
        id='gpt-4.1-mini'
    )
)

agent.print_response('Hi, how are you?')



from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .tools import search_gmail, search_drive, list_events

root_agent = Agent(
    name="workspace_assistant",
    model=LiteLlm(model="ollama_chat/llama3.1"),
    description="Answers questions using the user's Gmail, Drive, and Calendar.",
    instruction="Use the tools to look up real data before answering. Say when nothing was found. Never invent emails, files, or events.",
    tools=[search_gmail, search_drive, list_events],
)

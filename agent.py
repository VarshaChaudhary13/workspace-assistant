from google.adk.agents import Agent
from workspace_assistant.tools import search_gmail, search_drive, list_events

root_agent = Agent(
    name="workspace_assistant",
    model="gemini-2.0-flash",  # confirm the current model name in the docs
    description="Answers questions using the user's Gmail, Drive, and Calendar.",
    instruction="Use the tools to look up real data before answering. Say when nothing was found. Never invent emails, files, or events.",
    tools=[search_gmail, search_drive, list_events],
)
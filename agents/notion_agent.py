from autogen_agentchat.agents import AssistantAgent
from models.openai_model_client import get_openai_model_client
from config.prompt.system_prompt import SYSTEM_MESSAGE
from MCP.notion_mcp_tools import get_notion_mcp_tools



async def get_notion_agent():
    notion_mcp_tools = await get_notion_mcp_tools()
    model_client = get_openai_model_client()

    agent = AssistantAgent(
        name='notion_agent',
        model_client=model_client,
        system_message=SYSTEM_MESSAGE,
        tools=notion_mcp_tools,
        reflect_on_tool_use=True

    )
    return  agent
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
import streamlit as st
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

client=MultiServerMCPClient({
    "tools":{
        "url":"http://localhost:8000/mcp",
        "transport":"streamable_http"

    }
}
    
)


reAct_system_prompt="""
you are a ReAct style AI agent.
follow this steps carefully:
1.THOUGHT: think step by step about what to do next
2.ACTION:when needed, call one of the available tools
3.OBSERVATION:Read the tool results and decide your next step

Repeat THOUGHT->ACTION->OBSERVATION until you are ready to give the final answer.
"""

tools=asyncio.run(client.get_tools())

llm=init_chat_model(
    api_key=api_key,
    model="gpt-4o"

)
agent=create_agent(
    model=llm,
    tools=tools,
    system_prompt=reAct_system_prompt
    
)

st.title("AI AGENT with MCP")
task=st.text_input("Assign mme a Task")

if task:
    response=asyncio.run(agent.ainvoke({"messages":task}))
    final_response=response["messages"][-1]

    st.write(final_response.content)
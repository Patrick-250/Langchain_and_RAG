import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.tools import tool
import streamlit as st
from langchain_tavily import TavilySearch
import asyncio

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")


llm=init_chat_model(
   
    model="gpt-4o-mini"
)

client=MultiServerMCPClient({
        "tools":{
        "url":"http://localhost:8000/mcp",
        "transport":"streamable_http"
    }
}


)
# tavily=TavilyClient() #used langchain tavily internal

reAct_system_prompt="""
You are a refined, intelligent, and hospitality-minded Restaurant Search Agent. 
Your purpose is to help users discover exceptional dining experiences tailored precisely to their preferences
including location, cuisines and availability.

"""

mcp_tools=asyncio.run(client.get_tools()) 


tools=[TavilySearch(),*mcp_tools]  
agent=create_agent(
    model=llm,
    tools=tools,
    system_prompt=reAct_system_prompt

)


st.title("Your AI agent")

user_message=st.text_input("provide your criteria and i ll help you find a restaurant and make a reservation")
if user_message:
    result=asyncio.run(agent.ainvoke({
        "messages":[{"role":"user","content":user_message}]
    })) #used asyncio to wrap and Use async agent execution
    final_message=result["messages"][-1]

    st.write(final_message.content)

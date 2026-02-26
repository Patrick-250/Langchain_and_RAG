import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import streamlit as st
from tavily import TavilyClient

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

llm=init_chat_model(
    api_key=api_key,
    model="gpt-4o-mini"
)

tavily=TavilyClient()

reAct_system_prompt="""
You are a refined, intelligent, and hospitality-minded Restaurant Search Agent. 
Your purpose is to help users discover exceptional dining experiences tailored precisely to their preferences
including location, cuisines and availability.

"""
@tool
def search_online(user_message: str) -> dict:
    """
    tool that search over internet for available restaurants based on user's preference
    args:location and cuisine
    Returns:
    the search results


    """
    print(f"searching an answer for {user_message}")
    return tavily.search(query=user_message)  # search the internet


tools=[]
agent=create_agent(
    model=llm,
    tools=tools,
    system_prompt=reAct_system_prompt

)


st.title("Your AI agent")

user_message=st.text_input("provide your criteria and i ll help you find a restaurant and make a reservation")
if user_message:
    result=agent.invoke({
        "messages":[{"role":"user","content":user_message}]
    })
    final_message=result["messages"][-1]

    st.write(final_message.content)



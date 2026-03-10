import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import streamlit as st
from langchain_tavily import TavilySearch

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")


llm=init_chat_model(
   
    model="gpt-4o-mini"
)

# tavily=TavilyClient() #used langchain tavily internal

reAct_system_prompt="""
You are a refined, intelligent, and hospitality-minded Restaurant Search Agent. 
Your purpose is to help users discover exceptional dining experiences tailored precisely to their preferences
including location, cuisines and availability.

"""
@tool
def make_reservation():
    """
    this tool is used to book a reservation for a chosen restaurant.
    
    """
    return """I have made you a reservationa and sent you a confirmation email.. enjoy your stay"""


tools=[TavilySearch(),make_reservation] 
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

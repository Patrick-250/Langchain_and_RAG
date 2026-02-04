import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_community.agent_toolkits.load_tools import load_tools
import streamlit as st

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

llm=init_chat_model(
    api_key=api_key,
    model="gpt-4o-mini"
)

reAct_system_prompt="""
you are a ReAct style AI agent.
follow this steps carefully:
1.THOUGHT: think step by step about what to do next
2.ACTION:when needed, call one of the available tools
3.OBSERVATION:Read the tool results and decide your next step

Repeat THOUGHT->ACTION->OBSERVATION until you are ready to give the final answer.
"""
tools=load_tools(["wikipedia","ddg-search"])


agent=create_agent(
    model=llm,
    tools=tools,
    system_prompt=reAct_system_prompt

)

st.title("Your AI agent")

task=st.text_input("assign me something to do ")
if task:
    result=agent.invoke({
        "messages":[{"role":"user","content":task}]
    })
    final_message=result["messages"][-1]

    st.write(final_message.content)
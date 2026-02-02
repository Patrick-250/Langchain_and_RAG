import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.globals import set_debug



# set_debug(True)

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
model=os.getenv("MODEL_NAME")


llm=init_chat_model(
    api_key=api_key,
    model=model,
    max_tokens=200 #limit tokens to save money for now
)

template=PromptTemplate(
    variables=["location","budget_per_person","cuisine","number_of_people"],
    template="""
    you are a helpful assistant that  provide restaurant recommendation for the party based on user's {location},{budget_per_person},{cuisine},{number_of_people}
    {location} is the user's city of interest, {budget_per_person} is the maximum budget to be used by each person, {cuisine} is the cuisine type of interest
    (mexican,indian,american etc) and {number_of_people} is the total number of people attending. Avoid giving information about fictional places or cuisines.
    if the location or cuisine is  fictional please answer: I don't know

    answer as clear as possible with restaurants options to help the user choose the best one.
    """
)



st.title("Ask me about restaurant recommendations...")
location=st.text_input("what is your location of interest? ")
budget_per_person=st.number_input("what is your budget_per_person?")
cuisine=st.text_input("what is your cuisine of interest?")
number_of_people=st.number_input("How many people coming?")

# prompt=template.format(location=location,budget_per_person=budget_per_person,cuisine=cuisine,number_of_people=number_of_people)

chain=template | llm

if location and budget_per_person and cuisine and number_of_people:
    response=chain.invoke({"location":location,"budget_per_person":budget_per_person,"cuisine":cuisine,"number_of_people":number_of_people})
    st.write(response.content)
else:
    st.write("please provide all the fields")






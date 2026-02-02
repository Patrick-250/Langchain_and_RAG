import os

import streamlit as st

from dotenv import load_dotenv

from langchain.chat_models import init_chat_model

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_community.chat_message_histories import StreamlitChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = os.getenv("MODEL_NAME")

llm = init_chat_model(api_key=api_key, model=model, max_tokens=200)



if 'user_data' not in st.session_state:

    st.session_state.user_data = {}

if 'current_field' not in st.session_state:

    st.session_state.current_field = None

history_for_chain = StreamlitChatMessageHistory(key="chat_messages")

required_fields = ["location", "budget_per_person", "cuisine", "number_of_people"]

chat_template = ChatPromptTemplate.from_messages([

    ("system", """

You are a helpful assistant that provides restaurant recommendations based on user's requirements.

Avoid recommending fictional places or cuisines.

If the location or cuisine is fictional, reply: I don't know.

Answer as clearly as possible with restaurant options to help the user choose.

"""),

    MessagesPlaceholder(variable_name="chat_history"),

    ("human", """

Location: {location}

Budget per person: {budget_per_person}

Cuisine: {cuisine}

Number of people: {number_of_people}

""")

])

chain = chat_template | llm

chain_with_history = RunnableWithMessageHistory(

    chain,

    lambda session_id: history_for_chain,

    input_messages_key="location",

    history_messages_key="chat_history"

)

st.title("🍽️ Restaurant Recommendations")



for msg in history_for_chain.messages:

    if msg.type == "human":

        with st.chat_message("user"):

            st.write(msg.content)

    else:

        with st.chat_message("assistant"):

            st.write(msg.content)


user_input = st.chat_input("Type your message here...")

if user_input:



    with st.chat_message("user"):

        st.write(user_input)

    if st.session_state.current_field:


        st.session_state.user_data[st.session_state.current_field] = user_input

        st.session_state.current_field = None

    else:

      

        user_input_lower = user_input.lower()

      

        if "location" not in st.session_state.user_data:

            if " in " in user_input_lower:

                location = user_input.split(" in ")[-1].split(" for ")[0].strip()

                st.session_state.user_data["location"] = location

       

        if "number_of_people" not in st.session_state.user_data:

            if " for " in user_input_lower:

                import re

                match = re.search(r'for (\d+) people', user_input_lower)

                if match:

                    st.session_state.user_data["number_of_people"] = match.group(1)

  

        if "budget" in user_input_lower and "budget_per_person" not in st.session_state.user_data:

            words = user_input.split()

            for i, word in enumerate(words):

                if word.lower() == "budget" and i + 1 < len(words):

                    st.session_state.user_data["budget_per_person"] = words[i + 1]

  

        if "cuisine" not in st.session_state.user_data:

            cuisines = ["italian", "chinese", "japanese", "mexican", "indian", "french", "thai"]

            for cuisine in cuisines:

                if cuisine in user_input_lower:

                    st.session_state.user_data["cuisine"] = cuisine


    missing_fields = [f for f in required_fields if f not in st.session_state.user_data]

    if missing_fields:


        st.session_state.current_field = missing_fields[0]

        field_name = missing_fields[0].replace("_", " ").title()

        assistant_msg = f"Please provide your **{field_name}**."

        with st.chat_message("assistant"):

            st.write(assistant_msg)



        history_for_chain.add_user_message(user_input)

        history_for_chain.add_ai_message(assistant_msg)

    else:

     

        with st.chat_message("assistant"):

            with st.spinner("Finding restaurants..."):

                response = chain_with_history.invoke(

                    {

                        "location": st.session_state.user_data["location"],

                        "budget_per_person": st.session_state.user_data["budget_per_person"],

                        "cuisine": st.session_state.user_data["cuisine"],

                        "number_of_people": st.session_state.user_data["number_of_people"]

                    },

                    config={"configurable": {"session_id": "abc123"}}

                )

                st.write(response.content)


        st.session_state.user_data = {}

        st.session_state.current_field = None

    st.rerun()
 
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate


load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
model=os.getenv("MODEL_NAME")


llm=init_chat_model(
    api_key=api_key,
    model=model
)

template=PromptTemplate(
    variables=["technical_term"],
    template="provide a one line definition of {technical_term}"
)
technical_term=input("what Technical term would you wanna learn about?  ")
prompt=template.format(technical_term=technical_term)
response=llm.invoke(prompt)
print(response.content)


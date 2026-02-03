import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

embedding_model=OpenAIEmbeddings(api_key=api_key)

question1="the day is sunny with blue sky"
question2="it is a blue sky sunny day"

#gonna compare the similariuty between question1 and question2.... the embeddings looks kind more similar

embedding1=embedding_model.embed_query(question1)
print(embedding1)

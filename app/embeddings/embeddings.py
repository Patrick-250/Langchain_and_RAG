import os
import numpy as np
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

embedding_model=OpenAIEmbeddings(api_key=api_key)

question1="the day is sunny with blue sky"
question2="it is a blue sky sunny day"

#gonna compare the similariuty between question1 and question2.... the embeddings should looks kind more similar

embedding1=embedding_model.embed_query(question1)
# print(embedding1)

embedding2=embedding_model.embed_query(question2)
# print(embedding2)

similarity_score=np.dot(embedding1,embedding2) #between 0-1

print(similarity_score) #outputted 0.9653976068670587 meaning high similarity


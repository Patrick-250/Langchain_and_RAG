import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

embedding_model=OpenAIEmbeddings(api_key=api_key)

document=TextLoader("restaurants.txt").load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)

chunks=text_splitter.split_documents(document)

# print(chunks[0])

db=Chroma.from_documents(chunks,embedding_model)

question=input("Ask me about restaurant recommendation ")
question_embedding=embedding_model.embed_query(question)

matching_docs=db.similarity_search_by_vector(question_embedding)

for doc in matching_docs:
    print(doc.page_content)
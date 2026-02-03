import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

llm=init_chat_model(
    api_key=api_key,
    model="gpt-4o"
)

prompt_template=ChatPromptTemplate.from_messages(
    [("system","""you are a restaurant recommendor that help the user find the restaurant that matches their requirements.
    if the answer is not clear, acknowledge that you do not know. limit your answer to 2-4 consise sentences.{context}"""),
    ("human","{input}")
    ]
)

embedding_model=OpenAIEmbeddings(api_key=api_key)

document=TextLoader("restaurants.txt").load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)

chunks=text_splitter.split_documents(document)

# print(chunks[0])

vector_store=Chroma.from_documents(chunks,embedding_model)
retriever=vector_store.as_retriever()

qa_chain=create_stuff_documents_chain(llm=llm,prompt=prompt_template)
rag_chain=create_retrieval_chain(retriever,qa_chain)

print("ask me about restaurants ")
question=input("I can help you find a restaurant....")

if question:
    response=rag_chain.invoke({"input":question})
    print(response['answer'])
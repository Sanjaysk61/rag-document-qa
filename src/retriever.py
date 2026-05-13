import os 
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
from google import genai
from src.embedder import load_vector_store


load_dotenv(dotenv_path=Path(__file__).parent.parent/".env")
api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def ask_question(question:str , vector_store, k: int=3):

    relevant_chunks = vector_store.similarity_search(question, k=k)

    context = "\n\n".join([doc.page_content for doc in relevant_chunks])

    prompt = f""" your are a helpful assitant. Answer this only using the context provided below. 
    if the answer is not in the context, say "I don't have enough information to answer this."

    Context:{context}

    Question:{question}

    Answer:"""
    
    response = client.models.generate_content(
            model = "gemini-3-flash-preview" ,
            contents = prompt)
    
    return response.text, relevant_chunks

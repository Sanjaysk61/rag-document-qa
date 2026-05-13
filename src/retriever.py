import os
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

def get_client():
    """Creates Gemini client fresh each call — reads latest secret."""
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except Exception:
        api_key = os.getenv("GOOGLE_API_KEY")
    return genai.Client(api_key=api_key)

def ask_question(question: str, vector_store, k: int = 3):

    relevant_chunks = vector_store.similarity_search(question, k=k)

    context = "\n\n".join([doc.page_content for doc in relevant_chunks])

    prompt = f"""You are a helpful assistant. Answer the question using only the context provided below.
If the answer is not in the context, say "I don't have enough information to answer this."

Context:
{context}

Question: {question}

Answer:"""

    client = get_client()  # Fresh client every time
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text, relevant_chunks
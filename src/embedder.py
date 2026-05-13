from pathlib import Path
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(chunks):
    """
    Creates an in-memory ChromaDB vector store.
    No persist_directory — works both locally and on Streamlit Cloud.
    """
    print("Creating Embeddings and Storing in memory...")

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
        # No persist_directory — stays in RAM
    )

    print(f"Done! {len(chunks)} chunks stored in memory.")
    return vector_store


def load_vector_store():
    """
    No longer needed — vector store is rebuilt fresh each session.
    Kept for backward compatibility with local test scripts.
    """
    print("Note: On cloud, vector store is rebuilt per session.")
    return None
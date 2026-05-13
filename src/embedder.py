from pathlib import Path
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(chunks, persist_directory="chroma_db"):

    print("Creating Embeddings and Storing it in chroma_db")

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory
    )

    print(f"Done! {len(chunks)} chunks stored in chromaDB at '{persist_directory}'")
    return vector_store

def load_vector_store(persist_directory="chroma_db"):

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )

    print(f"Vector store loaded from '{persist_directory}'")
    return vector_store
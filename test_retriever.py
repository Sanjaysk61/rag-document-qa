from src.retriever import ask_question
from src.embedder import load_vector_store

vector_store = load_vector_store()

question = "What is the name of the student that submitted the project"

answer, sources = ask_question(question, vector_store )

print(f"\n Question:{question}")

print(f"\n Answer:{answer}")

print("\n ---source Used---")

for i, doc in enumerate(sources):
    print(f"\n Source{i+1}:{doc.page_content[:200]}...")



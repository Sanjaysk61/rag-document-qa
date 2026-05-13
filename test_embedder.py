from src.loader import load_and_chunk_pdf
from src.embedder import create_vector_store

# Load and chunk the PDF
chunks = load_and_chunk_pdf("data/sample.pdf")

# Create and save vector store
vector_store = create_vector_store(chunks)

# Test a search
query = "what is the research topic of this thesis"
results = vector_store.similarity_search(query, k=3)

print("\n--- Top 3 Relevant Chunks ---")
for i, doc in enumerate(results):
    print(f"\nResult {i+1}:")
    print(doc.page_content)
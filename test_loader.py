from src.loader import load_and_chunk_pdf

chunks = load_and_chunk_pdf("data/sample.pdf")

print(f"Total chunks ready for embedding:{len(chunks)}")
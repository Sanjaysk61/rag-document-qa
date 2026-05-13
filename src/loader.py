from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk_pdf(pdf_path: str):

    print(f"Loading Pdf :{pdf_path}")
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    print(f"Total Pages Loaded :{len(pages)}")

    splitter = RecursiveCharacterTextSplitter( chunk_size = 500,chunk_overlap = 50)
    chunks = splitter.split_documents(pages)

    print(f"Total Chunks Created:{len(chunks)}")
    print("\n ---Chunk Preview---")
    print(chunks[0].page_content)

    return chunks

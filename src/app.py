import os 
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))


import streamlit as st
from src.loader import load_and_chunk_pdf
from src.embedder import create_vector_store, load_vector_store
from src.retriever import ask_question


# Page config
st.set_page_config(page_title="RAG Document Q&A", page_icon="📄")
st.title("📄 Document Q&A with Gemini")
st.markdown("Upload a PDF and ask questions about it.")

# Sidebar for PDF upload
with st.sidebar:
    st.header("📁 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

    if uploaded_file:
        # Save uploaded file to data/ folder
        pdf_path = Path("data") / uploaded_file.name
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Uploaded: {uploaded_file.name}")

        # Process button
        if st.button("Process PDF"):
            with st.spinner("Loading and chunking PDF..."):
                chunks = load_and_chunk_pdf(str(pdf_path))

            with st.spinner("Creating embeddings..."):
                st.session_state.vector_store = create_vector_store(chunks)

            st.success(f"Done! {len(chunks)} chunks processed.")

# Main area — Q&A
if "vector_store" in st.session_state:
    st.header("💬 Ask a Question")

    question = st.text_input("Enter your question:")

    if st.button("Ask"):
        if question.strip():
            with st.spinner("Searching and generating answer..."):
                answer, sources = ask_question(question, st.session_state.vector_store)

            st.subheader("Answer")
            st.write(answer)

            with st.expander("📚 View Source Chunks"):
                for i, doc in enumerate(sources):
                    st.markdown(f"**Source {i+1}:**")
                    st.write(doc.page_content)
                    st.divider()
        else:
            st.warning("Please enter a question.")
else:
    st.info("👈 Upload and process a PDF from the sidebar to get started.")

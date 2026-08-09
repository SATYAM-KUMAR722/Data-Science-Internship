from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from utils.rag_loader import load_and_split_documents


CHROMA_DIR = "chroma_db"


def create_vector_store():

    # Load and split PDFs
    chunks = load_and_split_documents()

    print(f"Creating embeddings for {len(chunks)} chunks...")

    # Embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store embeddings in ChromaDB
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    print("ChromaDB created successfully!")

    return vector_store


if __name__ == "__main__":
    create_vector_store()
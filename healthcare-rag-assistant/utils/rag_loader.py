from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


DOCUMENTS_DIR = Path("documents")


def load_and_split_documents():

    documents = []

    for pdf_file in DOCUMENTS_DIR.glob("*.pdf"):

        print(f"Loading: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))

        pdf_documents = loader.load()

        documents.extend(pdf_documents)

    print(f"\nLoaded {len(documents)} pages.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    return chunks


if __name__ == "__main__":

    chunks = load_and_split_documents()

    for i, chunk in enumerate(chunks[:3]):

        print(f"\n--- Chunk {i + 1} ---")
        print(chunk.page_content[:500])
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


CHROMA_DIR = "chroma_db"


def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    question = "What are the ICU visiting hours?"

    results = retriever.invoke(question)

    print("\nRetrieved Documents:\n")

    for i, doc in enumerate(results):

        print(f"--- Result {i + 1} ---")
        print(doc.page_content)
        print("Metadata:", doc.metadata)
        print()
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils.retriever import get_retriever

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def ask_rag(question):

    # 1. Retrieve relevant chunks from ChromaDB
    retriever = get_retriever()
    documents = retriever.invoke(question)

    # 2. Check whether anything was retrieved
    if not documents:
        return (
            "I couldn't find this information in "
            "the available hospital policies."
        )

    # 3. Combine chunks with metadata
    context_parts = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        page = document.metadata.get(
            "page_label",
            "Unknown"
        )

        context_parts.append(
            f"""
Source: {source}
Page: {page}

Content:
{document.page_content}
"""
        )

    context = "\n\n".join(context_parts)

    # 4. Give retrieved context to Gemini
    prompt = f"""
You are a hospital policy assistant.

Answer the user's question using ONLY the
provided hospital policy context.

If the answer is not present in the context,
say that the information was not found in
the available hospital policies.

Do not invent information.

Hospital Policy Context:
{context}

User Question:
{question}

Provide:
1. A concise answer.
2. The source document and page supporting the answer.

Answer:
"""

    # 5. Generate answer
    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":

    question = input(
        "Ask a hospital policy question: "
    )

    answer = ask_rag(question)

    print("\nFinal Answer:")
    print(answer)
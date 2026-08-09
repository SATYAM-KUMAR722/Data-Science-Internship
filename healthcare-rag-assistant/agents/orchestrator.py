from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.sql_agent import ask_sql
from utils.rag_answer import ask_rag


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def route_question(question):

    prompt = f"""
You are a routing agent for a hospital information system.

There are two available systems:

SQL:
Used for structured patient data such as:
- patient count
- age
- gender
- medical condition
- billing amount
- medication
- admission information
- discharge information
- hospital information

RAG:
Used for hospital policy documents such as:
- ICU visiting hours
- visitor rules
- admission policy
- discharge policy
- medication policy
- infection control
- patient privacy
- staff conduct
- emergency procedures

Classify the user's question as exactly one of:

SQL
RAG

Return ONLY SQL or RAG.

User question:
{question}
"""

    response = llm.invoke(prompt)

    route = response.content.strip().upper()

    if "SQL" in route:
        return "SQL"

    return "RAG"


def ask_hospital(question):

    route = route_question(question)

    print(f"\nRoute selected: {route}")

    if route == "SQL":

        result = ask_sql(question)

        return {
            "route": "SQL",
            "result": result
        }

    else:

        result = ask_rag(question)

        return {
            "route": "RAG",
            "result": result
        }

    
if __name__ == "__main__":

    question = input("Ask a hospital question: ")

    result = ask_hospital(question)

    print("\nFinal Answer:")

    if result["route"] == "RAG":
        print(result["result"])

    elif result["route"] == "SQL":
        print(result["result"]["result"])
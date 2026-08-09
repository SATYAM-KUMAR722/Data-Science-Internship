from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.sql_tool import execute_sql

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def run_sql_agent(question):

    prompt = f"""
You are a SQL expert.

You are querying a SQLite database.

Table name:
patients

Exact columns:
- Name
- Age
- Gender
- Blood Type
- Medical Condition
- Date of Admission
- Doctor
- Hospital
- Insurance Provider
- Billing Amount
- Room Number
- Admission Type
- Discharge Date
- Medication
- Test Results

Rules:
1. Use ONLY the column names listed above.
2. Do not invent column names.
3. The disease column is exactly "Medical Condition".
4. Use double quotes around column names containing spaces.
5. Generate valid SQLite SQL.
6. Return ONLY the SQL query.
7. Do NOT use markdown code blocks.

User question:
{question}
"""

    response = llm.invoke(prompt)

    sql_query = response.content.strip()

    if sql_query.startswith("```"):
        sql_query = sql_query.split("\n", 1)[1]
        sql_query = sql_query.rsplit("```", 1)[0]

    sql_query = sql_query.strip()

    print("\nGenerated SQL:")
    print(sql_query)

    result = execute_sql(sql_query)

    return {
        "sql_query": sql_query,
        "result": result
    }


# Wrapper for the Orchestrator
def ask_sql(question):
    return run_sql_agent(question)
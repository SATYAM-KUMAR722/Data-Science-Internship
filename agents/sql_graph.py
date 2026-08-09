from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from agents.sql_agent import run_sql_agent


class SQLState(TypedDict):
    question: str
    sql_query: str
    result: str


def sql_node(state: SQLState):

    response = run_sql_agent(state["question"])

    return {
        "sql_query": response["sql_query"],
        "result": str(response["result"])
    }


graph = StateGraph(SQLState)

graph.add_node("sql_agent", sql_node)

graph.add_edge(START, "sql_agent")
graph.add_edge("sql_agent", END)

sql_graph = graph.compile()


if __name__ == "__main__":

    question = input("\nAsk a question about the patients: ")

    result = sql_graph.invoke({
        "question": question
    })

    print("\nFinal Result:")
    print(result["result"])
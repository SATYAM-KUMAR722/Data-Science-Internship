# RAG-Based Healthcare Query Assistant

AI-powered multi-agent application that allows hospital staff to query patient records and hospital policy documents using plain English. An Orchestrator Agent classifies every incoming query and routes it to either the NLP-to-SQL Agent, which answers data-driven questions against a synthetic patient database, or the RAG Agent, which retrieves answers from synthetically generated hospital policy documents. The project demonstrates a practical multi-agent architecture where structured and unstructured hospital knowledge becomes instantly accessible through a single conversational interface.

---

## Architecture

```
                 Orchestrator
                 /          \
                /            \
        ask_sql()           ask_rag()
            ↓                   ↓
     run_sql_agent()        Retriever
            ↓                   ↓
         SQLite             ChromaDB
            ↓                   ↓
       Patient data       Policy documents
```

---

## Project Structure

```
healthcare-rag-assistant/
├── agents/
│   ├── sql_agent.py        # NLP-to-SQL agent + ask_sql() wrapper
│   └── sql_graph.py
├── app/                    # Streamlit UI
├── data/
│   └── healthcare_dataset.csv
├── database/
│   └── hospital.db         # SQLite patient database
├── documents/
│   └── *.pdf               # Hospital policy documents
├── utils/
│   ├── database_loader.py
│   ├── rag_answer.py       # ask_rag() function
│   ├── rag_loader.py
│   ├── retriever.py
│   ├── sql_tool.py
│   └── vector_store.py
├── .env
├── requirements.txt
└── README.md
```

---

## Agents

| Agent | Function | Data Source |
|---|---|---|
| NLP-to-SQL Agent | Converts natural language to SQL and queries patient records | SQLite (`hospital.db`) |
| RAG Agent | Retrieves answers from hospital policy documents | ChromaDB + PDF documents |
| Orchestrator | Classifies the query and routes to the correct agent | — |

---

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd healthcare-rag-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=<your_google_api_key>
```

### 5. Load the patient database

```bash
python utils/database_loader.py
```

### 6. Build the vector store

```bash
python -m utils.vector_store
```

### 7. Run the app

```bash
streamlit run app/main.py
```

---

## Example Queries

**Patient data (SQL Agent)**
- "How many patients have diabetes?"
- "List all patients admitted in January 2024."
- "What is the average billing amount by insurance provider?"

**Hospital policy (RAG Agent)**
- "What is the visitor policy for ICU patients?"
- "What are the steps for patient discharge?"
- "What is the medication administration policy?"

---

## Tech Stack

- [LangChain](https://www.langchain.com/) — agent and chain orchestration
- [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) — LLM
- [ChromaDB](https://www.trychroma.com/) — vector store for policy documents
- [SQLite](https://www.sqlite.org/) — patient records database
- [Streamlit](https://streamlit.io/) — conversational UI
- [HuggingFace sentence-transformers](https://huggingface.co/sentence-transformers) — embeddings

# RAG-Based Healthcare Query Assistant

An AI-powered multi-agent application that allows hospital staff to query patient records and hospital policy documents using natural language.

The system uses an **Orchestrator Agent** to classify incoming queries and route them to the appropriate agent:

- **NLP-to-SQL Agent** – answers data-related questions using the patient database.
- **RAG Agent** – retrieves relevant information from hospital policy documents.

The project demonstrates how structured and unstructured healthcare information can be accessed through a single conversational interface.

## Features

- Multi-Agent Architecture
- Query routing using an Orchestrator Agent
- Natural Language to SQL
- Retrieval-Augmented Generation (RAG)
- Vector-based document retrieval
- Synthetic healthcare dataset
- SQLite database for patient records
- React + Vite frontend
- Python-based AI/backend components

## How It Works

```text
    User Query
        ↓
    Orchestrator Agent
        ↓
 ┌───────────────┬
 ↓               ↓
SQL Agent       RAG Agent
 ↓               ↓
Patient DB      Policy Documents
 ↓               ↓
 └────── Answer ──────┘
           ↓
         User
```

## Technologies Used

### Frontend

- React.js
- Vite
- JavaScript
- CSS

### Backend & AI

- Python
- Retrieval-Augmented Generation (RAG)
- Natural Language to SQL
- Multi-Agent Architecture
- Vector Search

### Database & Storage

- SQLite
- ChromaDB
- CSV
- PDF Documents
git status
## Disclaimer

This project uses **synthetic healthcare data and documents** for educational and demonstration purposes. It is not intended for real-world medical diagnosis, treatment, or clinical decision-making.  

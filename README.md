# 🧠 Document Intelligence Pipeline (Dummy Version)

A modular and containerized demo pipeline for extracting and querying cyber threat intelligence — powered by FastAPI, Streamlit, and Docker.  
This version uses **simulated (dummy) outputs** for demonstration purposes.

---

## 📦 Features

- 📄 **Semantic Search:** Enter a natural language question about threat intel campaigns
- 🌐 **Indicator Lookup:** Search for domains, IPs, emails, socials, etc.
- 🔗 **Graph Traversal:** Explore linked indicators across campaigns
- 🧠 **Pattern Detection:** Detect social media clusters (simulated)
- 📊 **Campaign Analysis:** Identify shared indicators
- 🕒 **Timeline Query:** View indicator relationships over time

---

## 🐳 Dockerized Architecture

.
├── app/
│ ├── routes/queries.py ← API endpoints (dummy data)
│ ├── streamlit_app.py ← Streamlit UI
│ └── (optional subfolders: db/, vector_store/, etc.)
├── Dockerfile
├── docker-compose.yml
└── README.md


- `FastAPI` serves the backend at [`http://localhost:8000`](http://localhost:8000)
- `Streamlit` serves the dashboard at [`http://localhost:8501`](http://localhost:8501)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>

docker compose up --build

 Access the UI
Open your browser: http://localhost:8501

Try out the search fields (you’ll get hardcoded responses)

 Test API Endpoints Directly
You can test any endpoint in your browser or Postman:

Semantic:
GET http://localhost:8000/queries/semantic?q=What Russian disinformation campaigns target France?

Indicator Lookup:
GET http://localhost:8000/queries/indicator_lookup?campaign=Doppelgänger

Known Limitations (Dummy Version)
No real data is extracted from PDFs

Embeddings, search, and graph queries are simulated

Neo4j, Qdrant, and Postgres are included but unused

Safe fallback structure for future logic upgrades

What's Ready for Next Upgrade?
You can plug in real logic easily into:

queries.py → use real functions from graph_queries.py, vector_store.py

process_documents.py → PDF parsing + embedding generation

db/ → Neo4j ingest and query

vector.index → store & search real semantic chunks

Authors & Credits
Assignment by: [Company Name or Instructor]

Developed by: Your Name

Tools used: Python, FastAPI, Streamlit, Docker, pyvis, Neo4j, FAISS


---


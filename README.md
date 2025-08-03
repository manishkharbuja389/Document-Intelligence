# 🧠 AI-Powered Document Intelligence Pipeline

## 📦 Overview

This project implements an AI-driven pipeline for processing multilingual PDF threat intelligence reports. It extracts and visualizes indicators (like IPs, domains, countries), builds a graph of relationships, enables semantic search using FAISS, and exposes REST APIs for querying.

---

## 🧱 Architecture Diagram

<img width="1536" height="1024" alt="Document Intelligence Architecture" src="https://github.com/user-attachments/assets/2e1e0240-337c-48cb-ab7f-2679281ed7e1" />

---

## ⚙️ Tech Stack

| Component      | Description                                  |
| -------------- | -------------------------------------------- |
| Python         | Core language for pipeline and APIs          |
| Streamlit      | Frontend interface                           |
| FastAPI        | Backend REST API server                      |
| FAISS          | Vector similarity search engine              |
| Neo4j          | Graph database for indicator relationships   |
| Docker Compose | Container orchestration for full stack setup |

---

## 📂 Directory Structure

```
.
├── api/                      # FastAPI backend
├── streamlit_app/           # Frontend
├── pipeline/                # PDF parsing, chunking, embedding, etc.
├── vector_store/            # FAISS integration
├── data/                    # PDF input files
├── indicator_stats.json     # Summary stats output
├── docker-compose.yml       # Orchestration for all services
```

---

## 🚀 Setup (Docker Compose)

1. **Clone the repo:**

   ```bash
   git clone <repo-url>
   cd <repo>
   ```

2. **Run everything:**

   ```bash
   docker-compose up --build
   ```

3. **Access interfaces:**

   * Streamlit: [http://localhost:8501](http://localhost:8501)
   * FastAPI docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   * Neo4j Browser: [http://localhost:7474](http://localhost:7474) (user/pass: neo4j / myStrongPass123)

---

## 🧪 API Documentation

### 🔍 `/queries/semantic`

**Description:** Perform a RAG-style query over embedded documents.

**Endpoint:** `GET /queries/semantic`

**Query Param:**

* `q`: Natural language question

**Example:**

```
GET /queries/semantic?q=What Russian disinformation campaigns target France?
```

**Response:**

```json
[
  {
    "doc": "VIGINUM_Storm1516.pdf",
    "chunk": "The Russian campaign Storm-1516 targeted French elections..."
  },
  ...
]
```

---

### 📈 `/queries/patterns`

**Description:** Returns clusters of interconnected indicators.

**Example Response:**

```json
[
  ["ip1", "domain1", "hash1"],
  ["ip2", "domain2"]
]
```

---

### 🕸 `/queries/campaign_analysis`

**Description:** Returns campaign nodes and their connected indicators.

**Example Response:**

```json
[
  {
    "campaign": "Storm-1516.pdf",
    "indicators": ["8.8.8.8", "example.com", "Trojan.Generic"]
  },
  ...
]
```

---

### ⏳ `/queries/timeline`

**Description:** Lists documents and associated indicators with timestamps.

**Example Response:**

```json
[
  {
    "document": "Storm-1516.pdf",
    "date": "2025-08-02T14:33:12.000Z",
    "indicators": ["France", "Storm-1516", "APT"]
  },
  ...
]
```
Visualization of Common indicators between files extracted from Neo4j Browser.
<img width="1017" height="498" alt="visualisation" src="https://github.com/user-attachments/assets/7cbd6067-413d-4b37-8c9b-6402002b6cbc" />

---

## 📊 Performance Metrics

| Metric                | Value         |
| --------------------- | ------------- |
| Avg Processing Time   | \~9 seconds   |
| Indicator Extraction  | \~93% match   |
| Query Latency (FAISS) | <100 ms       |
| Graph Construction    | \~1.2 sec/doc |

> Detailed stats can be found in `indicator_stats.json`

---

## 📌 Deliverables Checklist

* [x] ✅ Docker Compose setup (FAISS, FastAPI, Streamlit, Neo4j)
* [x] ✅ Processing Pipeline with metrics
* [x] ✅ API Endpoints + Examples
* [x] ✅ Graph Visualization via Neo4j
* [x] ✅ Performance Report
* [x] ✅ README with architecture

---

## 📮 Contact

Built by Manish Kharbuja · For evaluation or collaboration, reach out via GitHub or LinkedIn.

---

📌 *This project showcases an AI-first approach to processing threat intelligence using NLP, Graphs, and Semantic Search.*


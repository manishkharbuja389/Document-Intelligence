import os
from pipeline.pdf_extraction import extract_text_from_pdf
from pipeline.chunking import simple_chunking
from pipeline.embedding import embed_chunks
from pipeline.extract_indicators import extract_indicators
from vector_store.faiss_store import VectorStore

from py2neo import Graph, Node, Relationship
from datetime import datetime
import json

PDF_DIR = "./data"
EMBED_DIM = 384  # Embedding size for MiniLM-L12-v2

graph = Graph("bolt://neo4j:7687", auth=("neo4j", "myStrongPass123"))

def main():
    vector_db = VectorStore(dim=EMBED_DIM)
    all_stats = []

    for filename in os.listdir(PDF_DIR):
        if not filename.endswith(".pdf"):
            continue

        filepath = os.path.join(PDF_DIR, filename)
        print(f"Processing {filename}...")

        # 1. Extract text from PDF
        text = extract_text_from_pdf(filepath)

        # 2. Chunk text
        chunks = simple_chunking(text)

        # 3. Embed chunks
        embeddings = embed_chunks(chunks)

        # 4. Store in FAISS
        vector_db.add(embeddings, metas=[{"doc": filename, "chunk": chunk} for chunk in chunks])

        # 5. Extract indicators and add to graph
        indicators = extract_indicators(text)

        # Create campaign node
        campaign_node = Node("Campaign", name=filename)
        graph.merge(campaign_node, "Campaign", "name")

        for t, values in indicators.items():
            for value in set(values):
                indicator_node = Node("Indicator", type=t, value=value)
                graph.merge(indicator_node, "Indicator", "value")
                rel = Relationship(indicator_node, "PART_OF_CAMPAIGN", campaign_node)
                graph.merge(rel)

        # 6. Logging stats
        all_stats.append({
            "document": filename,
            "chunks": len(chunks),
            "indicators": {k: len(set(v)) for k, v in indicators.items()}
        })

    # 7. Output stats
    with open("./indicator_stats.json", "w") as f:
        json.dump(all_stats, f, indent=2)

    # 8. Save the FAISS vector index and metadata
    vector_db.save("vector.index", "meta.pkl")

    print("✔ All documents processed. Stats written to indicator_stats.json")

if __name__ == "__main__":
    main()

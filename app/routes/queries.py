# app/routes/queries.py
from fastapi import APIRouter
from sentence_transformers import SentenceTransformer
from vector_store.faiss_store import VectorStore
from db.graph_queries import (
    find_indicators_by_campaign,
    traverse_graph,
    detect_social_clusters,
    common_indicators_across_campaigns,
    indicator_timeline,
)
from typing import Optional

router = APIRouter(prefix="/queries")

model = None
vector_db = None

@router.on_event("startup")
def load_resources():
    global model, vector_db
    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    vector_db = VectorStore(dim=384)
    vector_db.load("vector.index")

@router.get("/semantic")
async def semantic_search(q: str):
    embedding = model.encode(q)
    results = vector_db.search(embedding, k=5)
    matches = [r["meta"]["chunk"] for r in results]
    answer = "\n---\n".join(matches)
    return {"query": q, "answer": answer}

@router.get("/indicator_lookup")
async def indicator_lookup(campaign: str, type: Optional[str] = None):
    indicators = find_indicators_by_campaign(campaign, type)
    return {"campaign": campaign, "type": type, "indicators": indicators}

@router.get("/graph_traversal")
async def graph_traversal(indicator: str, hops: int = 2):
    related = traverse_graph(indicator, hops=hops)
    return {"indicator": indicator, "hops": hops, "related_indicators": related}

@router.get("/pattern_detection")
async def pattern_detection(type: str = "social_media"):
    clusters = detect_social_clusters(type)
    return {"type": type, "clusters": clusters}

@router.get("/campaign_analysis")
async def campaign_analysis():
    indicators = common_indicators_across_campaigns()
    return {"indicators": indicators}

@router.get("/timeline_query")
async def timeline_query(indicator: str):
    timeline = indicator_timeline(indicator)
    return {"indicator": indicator, "timeline": timeline}

from fastapi import APIRouter

router = APIRouter(prefix="/search")

@router.get("")
def semantic_search(q: str):
    return {"query": q, "results": []}  # Placeholder
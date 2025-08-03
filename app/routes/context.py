from fastapi import APIRouter

router = APIRouter(prefix="/context")

@router.get("/{indicator}")
def get_context(indicator: str):
    return {"indicator": indicator, "context": "Context text here"}  # Placeholder

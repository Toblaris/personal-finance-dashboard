from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/health")
async def health():
    """
    Simple health endpoint used by CI and local checks.
    """
    return {"status": "ok", "env": settings.ENV}
from fastapi import APIRouter

from .health import health_router  # noqa: F401
from .search import search_router  # noqa: F401
from .evaluate import evaluate_router  # noqa: F401

api_router = APIRouter()
api_router.include_router(evaluate_router, prefix="/evaluate")
api_router.include_router(health_router, prefix="/health")
api_router.include_router(search_router, prefix="/search/text")
from fastapi import APIRouter

health_router = APIRouter()

# App health check
@health_router.get("")
def health():
    return {"status": "ok"}
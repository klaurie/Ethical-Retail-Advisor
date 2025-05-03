import subprocess
import os
import sys
import time
import signal
import uvicorn

from typing import Optional

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import api_router
from backend.models import CompanySearchRequest, CompanySearchResponse, EthicsScore, EthicsEvalRequest
from backend.services import search_company, evaluate_ethics

app = FastAPI()

# CORS middleware for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React app
        "http://localhost:8000",  # FastAPI app
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This includes all routers for different endpoints from the backend
app.include_router(api_router)


if __name__ == "__main__":
    app_host = os.getenv("APP_HOST", "0.0.0.0")
    app_port = int(os.getenv("APP_PORT", "8000"))
    reload = True

    uvicorn.run(app="main:app", host=app_host, port=app_port, reload=reload)


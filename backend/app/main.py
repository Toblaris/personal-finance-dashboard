from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.health import router as health_router
from app.core.config import settings

# Simple startup log for environment visibility
print(f"Starting API in {settings.ENV} mode")

app = FastAPI(
    title="Personal Finance API",
    debug=settings.ENV == "development"
)

# CORS middleware (origins left empty until needed)
allowed_origins = getattr(settings, "ALLOWED_ORIGINS", []) or []
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/v1")
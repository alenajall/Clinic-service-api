from fastapi import FastAPI
from app.models.user import User
from app.models.clinic import Clinic
from app.models.service import Service
from app.models.review import Review
from app.models.clinic_service import ClinicService

from app.api.routes import auth
from app.core.config import settings
from app.db.database import engine, Base

# Create database tables (For development only; use Alembic for production)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
)

app.include_router(auth.router, prefix=settings.API_V1_PREFIX)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "docs": "/docs",
    }

@app.get("/health")
def health_check():
    return {"status": "active"}
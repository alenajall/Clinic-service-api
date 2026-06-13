from fastapi import FastAPI
from app.core.config import settings
from app.db.database import Base, engine
from app.api.routes import auth, clinics, services, reviews

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=(
        "An open clinic-services directory for Sierra Leone. "
        "Search clinics by name, district and service to improve healthcare access. "
        "Aligned with SDG 3: Good Health and Well-being."
    ),
    version="1.0.0",
    contact={"name": "Group — Limkokwing University Sierra Leone"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
)

app.include_router(auth.router, prefix=settings.API_V1_PREFIX)
app.include_router(clinics.router, prefix=settings.API_V1_PREFIX)
app.include_router(services.router, prefix=settings.API_V1_PREFIX)
app.include_router(reviews.router, prefix=settings.API_V1_PREFIX)


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "service": settings.PROJECT_NAME, "docs": "/docs"}

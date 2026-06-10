import httpx
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.deps import require_role
from app.models.user import User, UserRole
from app.crud.clinic import clinic_crud
from app.schemas.clinic import ClinicCreate, ClinicRead, ClinicUpdate
from app.core.config import settings
router = APIRouter(prefix="/clinics", tags=["Clinics"])
@router.get("/", response_model=list[ClinicRead])
def list_clinics(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return clinic_crud.get_multi(db, skip=skip, limit=limit)
@router.get("/search", response_model=list[ClinicRead])
def search_clinics(
    q: str | None = Query(None, description="Search by clinic name"),
    district: str | None = Query(None, description="Filter by district"),
    service: str | None = Query(None, description="Filter by service"),
    db: Session = Depends(get_db),
):
    return clinic_crud.search(db, q=q, district=district, service=service)
@router.get("/{clinic_id}", response_model=ClinicRead)
def get_clinic(clinic_id: int, db: Session = Depends(get_db)):
    clinic = clinic_crud.get(db, clinic_id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic
@router.post("/", response_model=ClinicRead, status_code=status.HTTP_201_CREATED)
def create_clinic(payload: ClinicCreate, db: Session = Depends(get_db),
                  _: User = Depends(require_role(UserRole.admin, UserRole.clinic_admin))):
    return clinic_crud.create(db, payload)
@router.put("/{clinic_id}", response_model=ClinicRead)
def update_clinic(clinic_id: int, payload: ClinicUpdate, db: Session = Depends(get_db),
                  _: User = Depends(require_role(UserRole.admin, UserRole.clinic_admin))):
    clinic = clinic_crud.get(db, clinic_id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic_crud.update(db, clinic, payload)
@router.delete("/{clinic_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_clinic(clinic_id: int, db: Session = Depends(get_db),
                  _: User = Depends(require_role(UserRole.admin))):
    if not clinic_crud.get(db, clinic_id):
        raise HTTPException(status_code=404, detail="Clinic not found")
    clinic_crud.remove(db, clinic_id)
    return None
@router.get("/{clinic_id}/health-alerts")
async def clinic_health_alerts(clinic_id: int, db: Session = Depends(get_db)):
    """Async endpoint - pulls live external health feed"""
    clinic = clinic_crud.get(db, clinic_id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(settings.EXTERNAL_HEALTH_FEED_URL)
        feed = resp.json()
    return {"clinic": clinic.name, "district": clinic.district, "live_feed": feed}
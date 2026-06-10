from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.deps import require_role
from app.models.user import User, UserRole
from app.crud.service import service_crud
from app.schemas.service import ServiceCreate, ServiceRead, ServiceUpdate
router = APIRouter(prefix="/services", tags=["Services"])
@router.get("/", response_model=list[ServiceRead])
def list_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service_crud.get_multi(db, skip=skip, limit=limit)
@router.get("/{service_id}", response_model=ServiceRead)
def get_service(service_id: int, db: Session = Depends(get_db)):
    service = service_crud.get(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service
@router.post("/", response_model=ServiceRead, status_code=status.HTTP_201_CREATED)
def create_service(payload: ServiceCreate, db: Session = Depends(get_db),
                   _: User = Depends(require_role(UserRole.admin))):
    return service_crud.create(db, payload)
@router.put("/{service_id}", response_model=ServiceRead)
def update_service(service_id: int, payload: ServiceUpdate, db: Session = Depends(get_db),
                   _: User = Depends(require_role(UserRole.admin))):
    service = service_crud.get(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service_crud.update(db, service, payload)
@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(service_id: int, db: Session = Depends(get_db),
                   _: User = Depends(require_role(UserRole.admin))):
    if not service_crud.get(db, service_id):
        raise HTTPException(status_code=404, detail="Service not found")
    service_crud.remove(db, service_id)
    return None
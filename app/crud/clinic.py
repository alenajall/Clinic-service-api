from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.clinic import Clinic
from app.models.service import Service
from app.models.clinic_service import ClinicService
from app.schemas.clinic import ClinicCreate, ClinicUpdate
class CRUDClinic(CRUDBase[Clinic, ClinicCreate, ClinicUpdate]):
    def search(self, db: Session, q=None, district=None, service=None) -> list[Clinic]:
        query = db.query(Clinic).filter(Clinic.is_active.is_(True))
        if q:
            query = query.filter(Clinic.name.ilike(f"%{q}%"))
        if district:
            query = query.filter(Clinic.district.ilike(f"%{district}%"))
        if service:
            query = (query.join(ClinicService).join(Service)
                          .filter(Service.name.ilike(f"%{service}%")))
        return query.distinct().all()
clinic_crud = CRUDClinic(Clinic)
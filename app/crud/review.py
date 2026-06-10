from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewUpdate
class CRUDReview(CRUDBase[Review, ReviewCreate, ReviewUpdate]):
    def get_by_clinic(self, db: Session, clinic_id: int) -> list[Review]:
        return db.query(Review).filter(Review.clinic_id == clinic_id).all()
review_crud = CRUDReview(Review)
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.crud.review import review_crud
from app.schemas.review import ReviewCreate, ReviewRead, ReviewUpdate
router = APIRouter(prefix="/reviews", tags=["Reviews"])
@router.get("/clinic/{clinic_id}", response_model=list[ReviewRead])
def get_clinic_reviews(clinic_id: int, db: Session = Depends(get_db)):
    return review_crud.get_by_clinic(db, clinic_id)
@router.post("/", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
def create_review(payload: ReviewCreate, db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    review_data = payload.model_dump()
    review_data["user_id"] = current_user.id
    from app.models.review import Review
    review = Review(**review_data)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int, db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    review = review_crud.get(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    if review.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your review")
    review_crud.remove(db, id=review_id)
    return None
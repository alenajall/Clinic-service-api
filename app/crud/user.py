from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, obj_in: UserCreate) -> User:
        user = User(
            full_name=obj_in.full_name,
            email=obj_in.email,
            hashed_password=hash_password(obj_in.password),
            role=obj_in.role,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


user_crud = CRUDUser(User)
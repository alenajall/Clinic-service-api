from pydantic import BaseModel, EmailStr, ConfigDict, Field
from app.models.user import UserRole


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)
    role: UserRole = UserRole.patient


class UserUpdate(BaseModel):
    full_name: str | None = None
    password: str | None = None


class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: UserRole
    model_config = ConfigDict(from_attributes=True)
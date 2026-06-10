from pydantic import BaseModel, ConfigDict, Field
class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comment: str | None = None
    clinic_id: int
class ReviewUpdate(BaseModel):
    rating: int | None = Field(None, ge=1, le=5)
    comment: str | None = None
class ReviewRead(BaseModel):
    id: int
    rating: int
    comment: str | None = None
    clinic_id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)
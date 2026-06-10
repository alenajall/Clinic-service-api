from pydantic import BaseModel, ConfigDict
class ServiceCreate(BaseModel):
    name: str
    category: str
    description: str | None = None
class ServiceUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    description: str | None = None
class ServiceRead(BaseModel):
    id: int
    name: str
    category: str
    description: str | None = None
    model_config = ConfigDict(from_attributes=True)
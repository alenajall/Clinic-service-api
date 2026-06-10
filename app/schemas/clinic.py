from pydantic import BaseModel, ConfigDict
class ClinicCreate(BaseModel):
    name: str
    description: str | None = None
    district: str
    address: str | None = None
    clinic_type: str
    phone: str | None = None
    latitude: float | None = None
    longitude: float | None = None
class ClinicUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    district: str | None = None
    address: str | None = None
    clinic_type: str | None = None
    phone: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    is_active: bool | None = None
class ClinicRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    district: str
    address: str | None = None
    clinic_type: str
    phone: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
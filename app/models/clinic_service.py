from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class ClinicService(Base):
    __tablename__ = "clinic_services"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id", ondelete="CASCADE"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id", ondelete="CASCADE"), nullable=False)
    is_free = Column(Boolean, default=False, nullable=False)
    fee = Column(Float, nullable=True)

    clinic = relationship("Clinic", back_populates="services")
    service = relationship("Service", back_populates="clinics")
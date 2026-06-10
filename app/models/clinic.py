from sqlalchemy import Column, Integer, String, Float, Boolean, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Clinic(Base):
    __tablename__ = "clinics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, index=True)
    description = Column(Text, nullable=True)
    district = Column(String(80), nullable=False, index=True)
    address = Column(String(255), nullable=True)
    clinic_type = Column(String(50), nullable=False)
    phone = Column(String(30), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    services = relationship("ClinicService", back_populates="clinic",
                            cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="clinic",
                           cascade="all, delete-orphan")

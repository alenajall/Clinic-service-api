from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), unique=True, nullable=False, index=True)
    category = Column(String(80), nullable=False)
    description = Column(Text, nullable=True)

    clinics = relationship("ClinicService", back_populates="service",
                           cascade="all, delete-orphan")

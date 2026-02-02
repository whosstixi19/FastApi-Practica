from sqlalchemy import Column, String
from .database import Base

class Persona(Base):
    __tablename__ = "personas"

    cedula = Column(String(10), primary_key=True, index=True, nullable=False)
    nombre = Column(String(100), index=True, nullable=False)
    direccion = Column(String(200), index=True, nullable=True)


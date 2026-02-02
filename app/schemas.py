from pydantic import BaseModel
from typing import Optional

class PersonaBase(BaseModel):
    cedula: str
    nombre: str
    direccion: str
class PersonaCreate(PersonaBase):
    pass


class PersonaUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None

class Persona(PersonaBase):
    pass

    class Config:
        from_attributes = True

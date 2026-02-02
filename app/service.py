
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .repository import PersonaRepository
from . import models, schemas

class PersonaService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = PersonaRepository(db)

    def get_all(self):
        return self.repo.find_all()

    def get_by_cedula(self, cedula: str):
        return self.repo.find_by_cedula(cedula)

    def create(self, persona_data: schemas.PersonaCreate):
        # Business logic: Check if cedula already exists
        existing_persona = self.repo.find_by_cedula(persona_data.cedula)
        if existing_persona:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Persona with cedula '{persona_data.cedula}' already exists."
            )
        
        persona = models.Persona(**persona_data.model_dump())
        self.repo.save(persona)
        self.db.commit()
        self.db.refresh(persona)
        return persona

    def update(self, cedula: str, persona_data: schemas.PersonaUpdate):
        db_persona = self.repo.find_by_cedula(cedula)
        if not db_persona:
            return None
        
        update_data = persona_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_persona, key, value)
            
        self.repo.save(db_persona)
        self.db.commit()
        self.db.refresh(db_persona)
        return db_persona

    def delete(self, cedula: str):
        db_persona = self.repo.find_by_cedula(cedula)
        if db_persona:
            self.repo.delete(db_persona)
            self.db.commit()
            return True
        return False
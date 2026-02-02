from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, database, service

# This will create the database tables automatically on startup
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Persona CRUD FastAPI")

# Dependency to get Service
def get_persona_service(db: Session = Depends(database.get_db)):
    return service.PersonaService(db)

@app.get("/api/personas", response_model=List[schemas.Persona])
def read_personas(service: service.PersonaService = Depends(get_persona_service)):
    return service.get_all()

@app.get("/api/personas/{cedula}", response_model=schemas.Persona)
def read_persona(cedula: str, service: service.PersonaService = Depends(get_persona_service)):
    db_persona = service.get_by_cedula(cedula)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona not found")
    return db_persona

@app.post("/api/personas", response_model=schemas.Persona, status_code=status.HTTP_201_CREATED)
def create_persona(persona: schemas.PersonaCreate, service: service.PersonaService = Depends(get_persona_service)):
    return service.create(persona)

@app.put("/api/personas/{cedula}", response_model=schemas.Persona)
def update_persona(cedula: str, persona: schemas.PersonaUpdate, service: service.PersonaService = Depends(get_persona_service)):
    db_persona = service.update(cedula, persona)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona not found")
    return db_persona

@app.delete("/api/personas/{cedula}")
def delete_persona(cedula: str, service: service.PersonaService = Depends(get_persona_service)):
    if not service.delete(cedula):
        raise HTTPException(status_code=404, detail="Persona not found")
    return {"message": "Persona deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Lee la URL de la base de datos desde una variable de entorno.
# Se proporciona un valor predeterminado para desarrollo local si la variable no está configurada.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://PruebaFast:1234@localhost:5432/mi_base_datos")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia que usaremos en las rutas para abrir/cerrar la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
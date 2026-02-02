# 🚀 FastAPI CRUD - Persona API

## 📋 Descripción
API REST con FastAPI para gestionar personas (CRUD completo) usando PostgreSQL y SQLAlchemy con arquitectura en capas (Repository, Service, Controller).

---

## 🏗️ Arquitectura del Proyecto

```
fastApi/
├── app/
│   ├── __init__.py          # Inicialización del paquete
│   ├── main.py              # Punto de entrada (Controlador/Routes)
│   ├── database.py          # Configuración de base de datos
│   ├── models.py            # Modelos SQLAlchemy (ORM)
│   ├── schemas.py           # Schemas Pydantic (validación)
│   ├── repository.py        # Capa de acceso a datos
│   └── service.py           # Lógica de negocio
├── venv/                    # Entorno virtual
├── requirements.txt         # Dependencias
├── .env                     # Variables de entorno (crear)
└── README.md               # Este archivo
```

**Capas:**
- **Controller** (main.py): Endpoints HTTP
- **Service** (service.py): Lógica de negocio
- **Repository** (repository.py): Acceso a datos
- **Models** (models.py): Entidades de base de datos

---

## 📦 Dependencias (requirements.txt)

```
fastapi
uvicorn
SQLAlchemy
psycopg2-binary
python-dotenv
```

---

## ⚙️ COMANDOS INICIALES - CONFIGURACIÓN COMPLETA

### 1️⃣ Verificar Python instalado
```cmd
python --version
```
**Debe mostrar:** Python 3.x.x (mínimo 3.7)

---

### 2️⃣ Crear Entorno Virtual

**Opción A - CMD:**
```cmd
cd C:\Users\tixi4\Downloads\fastApi
python -m venv venv
```

**Opción B - PowerShell:**
```powershell
cd C:\Users\tixi4\Downloads\fastApi
python -m venv venv
```

---

### 3️⃣ Activar Entorno Virtual

**CMD:**
```cmd
venv\Scripts\activate
```

**PowerShell (si da error de políticas):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

**VERIFICACIÓN:** Debe aparecer `(venv)` al inicio de la línea

---

### 4️⃣ Instalar Dependencias

```cmd
pip install --upgrade pip
pip install -r requirements.txt
```

**Verificar instalación:**
```cmd
pip list
```

**Debe mostrar:**
- fastapi
- uvicorn
- sqlalchemy
- psycopg2-binary
- python-dotenv

---

## 🗄️ CONFIGURACIÓN DE BASE DE DATOS

### 1️⃣ Crear Base de Datos en PostgreSQL

**Abrir pgAdmin 4 o psql:**

```sql
CREATE DATABASE mi_base_datos;
```

### 2️⃣ Crear archivo `.env` en la raíz del proyecto

```cmd
cd C:\Users\tixi4\Downloads\fastApi
echo. > .env
```

**Editar `.env` y agregar:**
```env
DATABASE_URL=postgresql://PruebaFast:1234@localhost:5432/mi_base_datos
```

**Formato:**
```
postgresql://[usuario]:[contraseña]@[host]:[puerto]/[nombre_bd]
```

**Ejemplo con diferentes credenciales:**
```env
DATABASE_URL=postgresql://postgres:admin@localhost:5432/examen_db
```

---

## 🚀 EJECUTAR LA APLICACIÓN

### Método 1: Uvicorn directo (RECOMENDADO)
```cmd
cd C:\Users\tixi4\Downloads\fastApi
venv\Scripts\activate
uvicorn app.main:app --reload
```

### Método 2: Python directo
```cmd
cd C:\Users\tixi4\Downloads\fastApi
venv\Scripts\activate
python -m uvicorn app.main:app --reload
```

### Método 3: Sin activar venv
```cmd
cd C:\Users\tixi4\Downloads\fastApi
venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

**Si todo está bien, verás:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## 📡 ENDPOINTS DE LA API

**Base URL:** `http://127.0.0.1:8000`

| Método | Endpoint | Descripción | Body (JSON) |
|--------|----------|-------------|-------------|
| GET | `/api/personas` | Listar todas las personas | - |
| GET | `/api/personas/{cedula}` | Obtener persona por cédula | - |
| POST | `/api/personas` | Crear nueva persona | `{"cedula": "1234567890", "nombre": "Juan Pérez", "direccion": "Calle 123"}` |
| PUT | `/api/personas/{cedula}` | Actualizar persona | `{"nombre": "Juan Modificado", "direccion": "Nueva Dirección"}` |
| DELETE | `/api/personas/{cedula}` | Eliminar persona | - |

---

## 🧪 PROBAR LA API

### 1️⃣ Swagger UI (Interfaz Interactiva)
Abre en el navegador:
```
http://127.0.0.1:8000/docs
```

### 2️⃣ Con CURL

**Crear Persona:**
```cmd
curl -X POST "http://127.0.0.1:8000/api/personas" -H "Content-Type: application/json" -d "{\"cedula\":\"1234567890\",\"nombre\":\"Juan Perez\",\"direccion\":\"Calle 123\"}"
```

**Listar Todas:**
```cmd
curl http://127.0.0.1:8000/api/personas
```

**Obtener por Cédula:**
```cmd
curl http://127.0.0.1:8000/api/personas/1234567890
```

**Actualizar:**
```cmd
curl -X PUT "http://127.0.0.1:8000/api/personas/1234567890" -H "Content-Type: application/json" -d "{\"nombre\":\"Juan Modificado\"}"
```

**Eliminar:**
```cmd
curl -X DELETE http://127.0.0.1:8000/api/personas/1234567890
```

### 3️⃣ Con Postman
1. Importar la colección desde `/docs` como OpenAPI
2. Probar los endpoints

---

## 🔧 SOLUCIÓN DE PROBLEMAS COMUNES

### ❌ Error: "Import could not be resolved"

**Causa:** Paquetes no instalados

**Solución:**
```cmd
venv\Scripts\activate
pip install -r requirements.txt
```

**En VS Code:** Recargar ventana
- `Ctrl + Shift + P` → "Developer: Reload Window"

---

### ❌ Error: "could not connect to server"

**Causa:** PostgreSQL no está corriendo o credenciales incorrectas

**Solución:**
1. **Verificar PostgreSQL:**
   - Windows: Abrir "Servicios" → Buscar "PostgreSQL" → Iniciar
   - O abrir pgAdmin 4 (esto inicia el servidor)

2. **Verificar credenciales en `.env`:**
   ```env
   DATABASE_URL=postgresql://usuario:password@localhost:5432/mi_base_datos
   ```

3. **Probar conexión:**
   ```cmd
   psql -U postgres -d mi_base_datos
   ```

---

### ❌ Error: "Table does not exist" / No aparece en pgAdmin

**Causa:** Las tablas no se han creado

**Solución:**
La tabla se crea **automáticamente** cuando ejecutas la aplicación por primera vez:

```python
# En main.py línea 8
models.Base.metadata.create_all(bind=database.engine)
```

**Pasos:**
1. Ejecutar la aplicación: `uvicorn app.main:app --reload`
2. Esperar a que cargue completamente
3. Refrescar en pgAdmin: Click derecho en "Tables" → "Refresh"
4. Debe aparecer tabla `personas`

**Verificar manualmente en psql:**
```sql
\c mi_base_datos
\dt
SELECT * FROM personas;
```

---

### ❌ Error: "scripts está deshabilitada" (PowerShell)

**Causa:** Política de ejecución de PowerShell

**Solución:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Alternativa:** Usar CMD en lugar de PowerShell

---

### ❌ Error: "Port 8000 already in use"

**Causa:** Otra instancia está corriendo

**Solución:**
1. **Cerrar procesos:**
   ```cmd
   netstat -ano | findstr :8000
   taskkill /PID [número_PID] /F
   ```

2. **Usar otro puerto:**
   ```cmd
   uvicorn app.main:app --reload --port 8001
   ```

---

### ❌ Error: "ModuleNotFoundError: No module named 'app'"

**Causa:** Ejecutando desde directorio incorrecto

**Solución:**
```cmd
cd C:\Users\tixi4\Downloads\fastApi
uvicorn app.main:app --reload
```

**Nota:** Debes estar en la carpeta `fastApi/`, NO en `fastApi/app/`

---

### ❌ Error: Entorno virtual corrupto

**Síntoma:** `python.exe` no encontrado en venv

**Solución:** Recrear entorno virtual
```cmd
cd C:\Users\tixi4\Downloads\fastApi
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧪 VERIFICAR QUE TODO FUNCIONA

### Checklist antes del examen:

```cmd
# 1. Verificar Python
python --version

# 2. Activar entorno
cd C:\Users\tixi4\Downloads\fastApi
venv\Scripts\activate

# 3. Verificar paquetes instalados
pip list | findstr -i "fastapi sqlalchemy uvicorn psycopg2 dotenv"

# 4. Verificar PostgreSQL
psql -U PruebaFast -d mi_base_datos -c "\dt"

# 5. Ejecutar aplicación
uvicorn app.main:app --reload

# 6. Probar en navegador
# Abrir: http://127.0.0.1:8000/docs

# 7. Crear persona de prueba desde /docs

# 8. Verificar en pgAdmin
# Ver tabla "personas" debe tener el registro
```

---

## 📝 COMANDOS RÁPIDOS DE EMERGENCIA

```cmd
# Reinstalar todo desde cero
cd C:\Users\tixi4\Downloads\fastApi
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# Recrear base de datos
psql -U postgres
DROP DATABASE mi_base_datos;
CREATE DATABASE mi_base_datos;
\q

# Ejecutar aplicación
uvicorn app.main:app --reload
```

---

## 🔍 ESTRUCTURA DE CÓDIGO

### models.py (Base de Datos)
```python
class Persona(Base):
    __tablename__ = "personas"
    cedula = Column(String(10), primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(200))
```

### schemas.py (Validación)
```python
class PersonaCreate(BaseModel):
    cedula: str
    nombre: str
    direccion: str
```

### repository.py (Acceso a Datos)
```python
def find_by_cedula(self, cedula: str):
    return self.db.query(models.Persona).filter(...).first()
```

### service.py (Lógica de Negocio)
```python
def create(self, persona_data):
    # Valida que no exista
    # Guarda en BD
    # Retorna resultado
```

### main.py (API Endpoints)
```python
@app.post("/api/personas")
def create_persona(persona: PersonaCreate):
    return service.create(persona)
```

---

## 💡 TIPS PARA EL EXAMEN

1. **Antes de empezar:**
   - Verifica PostgreSQL corriendo
   - Activa el entorno virtual
   - Ejecuta `pip list` para confirmar paquetes

2. **Si algo falla:**
   - Lee el error completo
   - Busca en la sección "Solución de Problemas"
   - No entres en pánico, sigue los pasos

3. **Durante desarrollo:**
   - Usa `/docs` para probar endpoints
   - Verifica en pgAdmin después de cada operación
   - El flag `--reload` recarga automáticamente cambios

4. **Comandos esenciales:**
   ```cmd
   # Activar venv
   venv\Scripts\activate
   
   # Ejecutar app
   uvicorn app.main:app --reload
   
   # Ver logs en consola para errores
   ```

---

## 📚 RECURSOS

- **Documentación FastAPI:** https://fastapi.tiangolo.com/
- **SQLAlchemy:** https://docs.sqlalchemy.org/
- **Pydantic:** https://docs.pydantic.dev/

---

## ✅ ÚLTIMA VERIFICACIÓN

```cmd
# Ejecutar estos comandos en orden:
cd C:\Users\tixi4\Downloads\fastApi
venv\Scripts\activate
python --version
pip list
uvicorn app.main:app --reload
```

**Si ves el servidor corriendo en http://127.0.0.1:8000 → ¡TODO ESTÁ LISTO! ✅**

---

**Creado para:** Examen FastAPI + PostgreSQL  
**Fecha:** Febrero 2026  
**Versión:** 1.0
"# FastApi-Practica" 

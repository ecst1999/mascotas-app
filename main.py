from fastapi import FastAPI
from routes.mascota_routes import mascota_router
from routes.galeria_routes import galeria_router
from routes.persona_routes import persona_router
from routes.solicitud_routes import solicitud_router
from routes.auth_routes import auth_router
from config.database import engine, Base
from config.setters import RoleSetter
from config.database import Session
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.title = 'Backend de app mascotas'
app.version = '0.0.1'

app.include_router(mascota_router)
app.include_router(galeria_router)
app.include_router(persona_router)
app.include_router(solicitud_router)
app.include_router(auth_router)
app.mount("/storage", StaticFiles(directory="storage"), name="storage")

Base.metadata.create_all(bind=engine)

# @app.on_event("startup")
# async def startup_event():
#     db = Session()
#     RoleSetter(db).set_roles()


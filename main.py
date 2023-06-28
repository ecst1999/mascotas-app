from fastapi import FastAPI
from routes.mascota import mascota_router
from config.database import engine, Base

app = FastAPI()
app.title = 'Backend de app mascotas'
app.version = '0.0.1'

app.include_router(mascota_router)

Base.metadata.create_all(bind=engine)
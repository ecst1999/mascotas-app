from fastapi import Path, APIRouter
from fastapi.responses import JSONResponse
from models.mascota import Mascota
from config.database import Session
from services.mascota import MascotaService
from fastapi.encoders import jsonable_encoder

mascota_router = APIRouter()

@mascota_router.get('/mascotas')
def get_mascotas():
    db = Session()
    result = MascotaService(db).get_mascotas()
    return JSONResponse( status_code=200, content= jsonable_encoder(result))
    
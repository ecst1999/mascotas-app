from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from services.mascota_service import MascotaService
from fastapi.encoders import jsonable_encoder
from schemas.mascota_schema import Mascota

mascota_router = APIRouter()

@mascota_router.get('/mascotas', tags=['mascotas'])
def get_mascotas():
    db = Session()
    result = MascotaService(db).get_mascotas()
    return JSONResponse( status_code=200, content= jsonable_encoder(result))
    

@mascota_router.post('/mascotas', tags=['mascotas'])
def add_mascota(mascota: Mascota):
    db = Session()
    MascotaService(db).add_mascota(mascota)
    return JSONResponse(status_code=201, content={"message": "Se registro la mascota de forma adecuada"})

@mascota_router.get('/mascotas/{id}', tags=['mascotas'])
def get_mascota(id: int):
    db = Session()
    result = MascotaService(db).get_mascota(id)
    return JSONResponse(status_code=201, content=jsonable_encoder(result))

@mascota_router.put('/mascotas/{id}', tags=['mascotas'])
def update_mascota(id: int, mascota: Mascota):
    db = Session()
    MascotaService(db).update_mascota(id, mascota)
    return JSONResponse(status_code=201, content={"message": "Se actualizo la mascota de forma adecuada"})

@mascota_router.delete('/mascotas/{id}', tags=['mascotas'])
def delete_mascotas(id: int):
    db = Session()
    MascotaService(db).delete_mascota(id)
    return JSONResponse(status_code=201, content={"message": "Se elimino la mascota de forma adecuada"})
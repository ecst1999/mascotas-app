from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from config.database import Session
from services.mascota_service import MascotaService
from fastapi.encoders import jsonable_encoder
from schemas.mascota_schema import Mascota
from helpers.jwt import validate_token, reuseable_oauth

mascota_router = APIRouter()

@mascota_router.get('/mascotas-p', tags=['mascotas'])
def get_mascotas_personas(token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = MascotaService(db).get_mascotas_personas(persona=payload['per'])
    return JSONResponse( status_code=200, content= jsonable_encoder(result))

@mascota_router.get('/mascotas', tags=['mascotas'])
def get_mascotas(token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = MascotaService(db).get_mascotas()
    return JSONResponse( status_code=200, content= jsonable_encoder(result))
    

@mascota_router.post('/mascotas', tags=['mascotas'])
def add_mascota(mascota: Mascota, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    MascotaService(db).add_mascota(mascota, persona=payload['per'])
    return JSONResponse(status_code=201, content={"message": "Se registro la mascota de forma adecuada"})

@mascota_router.get('/mascotas/{id}', tags=['mascotas'])
def get_mascota(id: int, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"}) 
    db = Session()
    result = MascotaService(db).get_mascota(id)
    return JSONResponse(status_code=201, content=jsonable_encoder(result))

@mascota_router.put('/mascotas/{id}', tags=['mascotas'])
def update_mascota(id: int, mascota: Mascota, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})    
    db = Session()
    MascotaService(db).update_mascota(id, mascota, persona=payload['per'])
    return JSONResponse(status_code=201, content={"message": "Se actualizo la mascota de forma adecuada"})

@mascota_router.delete('/mascotas/{id}', tags=['mascotas'])
def delete_mascotas(id: int, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})    
    db = Session()
    MascotaService(db).delete_mascota(id, payload['per'])
    return JSONResponse(status_code=201, content={"message": "Se elimino la mascota de forma adecuada"})
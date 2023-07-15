from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from config.database import Session
from services.solicitud_service import SolicitudService
from services.mascota_service import MascotaService
from schemas.solicitud_schema import Solicitud
from fastapi.encoders import jsonable_encoder
from helpers.jwt import validate_token, reuseable_oauth

solicitud_router = APIRouter()

@solicitud_router.get('/solicitudes', tags=['solicitudes'])
def get_solicitudes(token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = SolicitudService(db).get_solicitudes(payload['per'])
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))

@solicitud_router.get('/solicitudes-p', tags=['solicitudes'])
def get_solicitudes_mascotas(token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    mascotas_personas = MascotaService(db).get_mascotas_personas(payload['per'])    
    if not mascotas_personas:
        return JSONResponse(status_code=404, content={"msg": "No se encontraron mascotas"})
    result = []
    for mascota in mascotas_personas:
        result.append(SolicitudService(db).get_solicitudes_mascotas(mascota.pet_id)) 
    return JSONResponse(status_code= 200, content= jsonable_encoder(result[0]))

@solicitud_router.post('/solicitudes', tags=['solicitudes'])
def add_solicitud(solicitud: Solicitud, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    SolicitudService(db).add_solicitud(solicitud, payload['per'])
    return JSONResponse(status_code=201, content={"message": "Se registro la solicitud de forma adecuada"})

@solicitud_router.put('/solicitudes/{id}', tags=['solicitudes'])
def update_solicitud(id: int, solicitud: Solicitud, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = SolicitudService(db).get_solicitud(id, payload['per'])
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    SolicitudService(db).update_solicitud(id, solicitud, payload['per'])
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el campo de solicitud"})

@solicitud_router.get('/solicitudes/{id}', tags=['solicitudes'])
def get_solicitud(id: int, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = SolicitudService(db).get_solicitud(id, payload['per'])
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@solicitud_router.delete('/solicitudes/{id}', tags=['solicitudes'])
def delete_solicitud(id: int, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = SolicitudService(db).get_solicitud(id, payload['per'])
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    SolicitudService(db).delete_solicitud(id, payload['per'])
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro de solicitud"})


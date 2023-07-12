from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from config.database import Session
from schemas.persona_schema import Persona
from services.persona_service import PersonaService
from fastapi.encoders import jsonable_encoder
from helpers.jwt import validate_token, reuseable_oauth

persona_router = APIRouter()

@persona_router.get('/personas', tags=['personas'])
def get_personas(token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = PersonaService(db).get_personas()
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))

@persona_router.get('/persona/{id}', tags=['personas'])
def get_persona(id:int, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = PersonaService(db).get_persona(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))

@persona_router.put('/persona/{id}', tags=['personas'])
def update_persona(id: int, persona: Persona, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = PersonaService(db).get_persona(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    PersonaService(db).update_persona(id, persona, payload['per'])

    return JSONResponse(status_code=200, content={"message": "Se ha modificado el campo de persona"})

@persona_router.delete('/persona/{id}', tags=['personas'])
def delete_persona(id: int, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = PersonaService(db).get_persona(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    PersonaService(db).delete_persona(id)

    return JSONResponse(status_code=200, content={"message": "Se ha borrado a la persona"})
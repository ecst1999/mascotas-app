from fastapi import APIRouter, Depends, UploadFile, File, Form
import shutil
from fastapi.responses import JSONResponse
from config.database import Session
from services.persona_service import PersonaService
from fastapi.encoders import jsonable_encoder
from schemas.persona_schema import Persona
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

@persona_router.put('/persona', tags=['personas'])
def update_persona(persona: Persona, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})     

    db = Session()
    result = PersonaService(db).get_persona(payload['per'])
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    print(persona)
    PersonaService(db).update_persona(persona, payload['per'])

    return JSONResponse(status_code=200, content={"message": "Se ha modificado el campo de persona"})

@persona_router.delete('/persona-act/{id}', tags=['personas'])
def activate_persona(id: int):
    db = Session()    
    result = PersonaService(db).get_persona(payload['per'])
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    PersonaService(db).activar_cuenta(id)
    return JSONResponse(status_code=200, content={"message": "Se ha activo la cuenta de la persona"})

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
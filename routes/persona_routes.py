from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from schemas.persona_schema import Persona
from services.persona_service import PersonaService
from fastapi.encoders import jsonable_encoder

persona_router = APIRouter()

@persona_router.get('/personas')
def get_personas():
    db = Session()
    result = PersonaService(db).get_personas()
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))

@persona_router.get('/persona/{id}', tags=['personas'])
def get_persona(id:int):
    db = Session()
    result = PersonaService(db).get_persona(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))


@persona_router.post('/personas', tags=['personas'], response_model=dict, status_code=201)
def add_persona(persona: Persona):
    db = Session()
    PersonaService(db).add_personas(persona)
    return JSONResponse(status_code=201, content={"message": "Se registro la persona de forma adecuada"})

@persona_router.put('/persona/{id}', tags=['personas'])
def update_persona(id: int, persona: Persona):
    db = Session()
    result = PersonaService(db).get_persona(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    PersonaService(db).update_persona(id, persona)

    return JSONResponse(status_code=200, content={"message": "Se ha modificado el campo de persona"})

@persona_router.delete('/persona/{id}', tags=['personas'])
def delete_persona(id: int):
    db = Session()
    result = PersonaService(db).get_persona(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    PersonaService(db).delete_persona(id)

    return JSONResponse(status_code=200, content={"message": "Se ha borrado a la persona"})
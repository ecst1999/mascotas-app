from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.auth_service import AuthService
from config.database import Session
from schemas.usuario_schema import Usuario, UsuarioLogin
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter()

@auth_router.post('/register', tags=['auth'], response_model=dict, status_code=201)
def register(usuario: Usuario):
    if not password_equals(usuario.dict()["repeat_password"], usuario.dict()["usr_password"]):
        return JSONResponse(status_code=404, content={"message": "La contraseñas no coinciden"})        
    db = Session()
    AuthService(db).register(usuario)
    return JSONResponse(status_code=201, content={"message": "Se registro el usuario de forma adecuada"})


def password_equals(password, repeat_password)-> bool:
    if password == repeat_password:
        return True
    return False

@auth_router.post('/login', tags=['auth'], status_code=200)
def login(usuario: UsuarioLogin):    
    db = Session()
    valor = AuthService(db).login(usuario)
    return JSONResponse(status_code=200, content=jsonable_encoder(valor))

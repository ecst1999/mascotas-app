from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from services.usuario_service import UsuarioService
from fastapi.encoders import jsonable_encoder

usuario_router = APIRouter()

@usuario_router.get('/usuarios')
def get_roles():
    db = Session()
    result = UsuarioService(db).get_usuarios()
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))
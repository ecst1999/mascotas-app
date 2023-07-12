from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from services.usuario_service import UsuarioService
from fastapi.encoders import jsonable_encoder

usuario_router = APIRouter()

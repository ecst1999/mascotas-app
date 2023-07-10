from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from services.solicitud_service import SolicitudService
from fastapi.encoders import jsonable_encoder

solicitud_router = APIRouter()

@solicitud_router.get('/solicitudes', tags=['solicitudes'])
def get_solicitudes():
    db = Session()
    result = SolicitudService(db).get_solicitudes()
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))
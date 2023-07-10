from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.galeria_service import GaleriaService
from config.database import Session

from fastapi.encoders import jsonable_encoder

galeria_router = APIRouter()

@galeria_router.get('/galerias', tags=['galerias'])
def get_galerias():
    db = Session()
    result = GaleriaService(db).get_galerias()
    return JSONResponse( status_code=200, content= jsonable_encoder(result))
    
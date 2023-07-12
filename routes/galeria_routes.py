from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from services.galeria_service import GaleriaService
from services.galeria_service import Galeria
from config.database import Session

import shutil
from pathlib import Path

from fastapi.encoders import jsonable_encoder

galeria_router = APIRouter()

@galeria_router.get('/galerias', tags=['galerias'])
def get_galerias():
    db = Session()
    result = GaleriaService(db).get_galerias()
    return JSONResponse( status_code=200, content= jsonable_encoder(result))


@galeria_router.post('/galerias', tags=['galerias'])
def add_galerias(upload_file: UploadFile = File(...)):    
    db = Session()
    pathGuardar = f"storage/{upload_file.filename}"
    # GaleriaService(db).add_galeria(galeria)
    try:
        with open(pathGuardar, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()
    return {"filename": pathGuardar}
    

@galeria_router.get('/galeria{id}', tags=['galerias'])
def get_galeria(id: int):
    db = Session()
    result = GaleriaService(db).get_galeria(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    return JSONResponse(status_code=404, content=jsonable_encoder(result))
    
@galeria_router.put('/galeria/{id}', tags=['galerias'])
def update_galeria(id: int, galeria: Galeria):
    db = Session()
    result = GaleriaService(db).get_galeria(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    GaleriaService(db).update_galeria(id, galeria)
    return JSONResponse(status_code=201, content={"message": "Se actualizo la galeria de forma adecuada"})

@galeria_router.delete('/galeria/{id}', tags=['galerias'])
def delete_galeria(id: int):
    db = Session()
    result = GaleriaService(db).get_galeria(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    GaleriaService(db).delete_galeria(id)
    return JSONResponse(status_code=201, content={"message": "Se elimino la galeria de forma adecuada"})

from fastapi import APIRouter, UploadFile, File, Depends, Form
from fastapi.responses import JSONResponse
from services.galeria_service import GaleriaService
from services.galeria_service import Galeria
from config.database import Session
from helpers.jwt import validate_token, reuseable_oauth


import shutil
from pathlib import Path

from fastapi.encoders import jsonable_encoder

galeria_router = APIRouter()

@galeria_router.get('/galeria', tags=['galerias'])
def get_galerias(token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = GaleriaService(db).get_galerias()
    return JSONResponse( status_code=200, content= jsonable_encoder(result))


@galeria_router.post('/galeria', tags=['galerias'])
def add_galerias(pet: int = Form(), token: str = Depends(reuseable_oauth), galeriaImagen: UploadFile = File(...)):    
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    pathGuardar = f"storage/{galeriaImagen.filename}"
    try:
        with open(pathGuardar, "wb") as buffer:
            shutil.copyfileobj(galeriaImagen.file, buffer)
    finally:
        galeriaImagen.file.close()
    GaleriaService(db).add_galeria(galeriaImagen.filename, pathGuardar, pet)    
    return JSONResponse(status_code=201, content={"message": "Se guardo la imagen de forma adecuada"})

    

@galeria_router.get('/galeria/{id}', tags=['galerias'])
def get_galeria(id: int, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = GaleriaService(db).get_galeria(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    return JSONResponse(status_code=404, content=jsonable_encoder(result))
    
@galeria_router.put('/galeria/{id}', tags=['galerias'])
def update_galeria(id: int, token: str = Depends(reuseable_oauth), galeriaImagen: UploadFile = File(...)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()    
    result = GaleriaService(db).get_galeria(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    pathGuardar = f"storage/{galeriaImagen.filename}"
    try:
        with open(pathGuardar, "wb") as buffer:
            shutil.copyfileobj(galeriaImagen.file, buffer)
    finally:
        galeriaImagen.file.close()    
    GaleriaService(db).update_galeria(id, galeriaImagen.filename, pathGuardar)
    return JSONResponse(status_code=201, content={"message": "Se actualizo la galeria de forma adecuada"})

@galeria_router.delete('/galeria/{id}', tags=['galerias'])
def delete_galeria(id: int, token: str = Depends(reuseable_oauth)):
    payload = validate_token(token)
    if not payload:
        return JSONResponse(status_code=500, content={"msg": "El token no es valido, por favor inicie sesión"})
    db = Session()
    result = GaleriaService(db).get_galeria(id)
    if not result:
        return JSONResponse(status_code=404, content={"msg": "No encontrado"})
    GaleriaService(db).delete_galeria(id)
    return JSONResponse(status_code=201, content={"message": "Se elimino la galeria de forma adecuada"})

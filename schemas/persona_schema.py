from typing import Optional
from pydantic import BaseModel, Field


class Persona(BaseModel):
    per_identificacion: str = Field(min_length=10, max_length=20)
    per_nombre: str = Field(min_length=1, max_length=100)
    per_apellido: str = Field(min_length=1, max_length=100)         
    per_telefono: str = Field(min_length=10, max_length=15)
    per_correo: str = Field(min_length=1, max_length=75)
    per_direccion: str = Field(min_length=1, max_length=250)

    class Config:
        schema_extra = {
            "example": {                                
                "per_identificacion": "Identificacion",
                "per_nombre": "Nombre",
                "per_apellido": "Apellido",
                "per_telefono": "0987654321",
                "per_correo": "correo@mail.com",
                "per_direccion": "Direccion"   
            }
        }
from typing import Optional
from pydantic import BaseModel, Field

class Galeria(BaseModel):

    gal_nombre: str = Field(min_length=1, max_length=100) 
    gal_pathImagen: str = Field(min_length=1, max_length=100)    
    pet_id: int = Field()


    class Config:
        schema_extra = {
            "example": {                                
                "gal_nombre": "Nombre galeria",
                "gal_pathImagen": "Path imagen",
                "pet_id": 0,
            }
        }
from typing import Optional
from pydantic import BaseModel, Field

class Mascota(BaseModel):
        
    pet_nombre: str = Field(min_length=1, max_length=100)
    pet_especie: str = Field(min_length=1, max_length=100)
    pet_edad: str = Field(min_length=1, max_length=3)        

    class Config:
        schema_extra = {
            "example": {                                
                "pet_nombre": "Nombre mascota",
                "pet_especie": "Especie mascota",
                "pet_edad": 5                
            }
        }
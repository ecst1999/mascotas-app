from typing import Optional
from pydantic import BaseModel, Field

class Solicitud(BaseModel):

    sol_descripcion: str = Field(min_length=5, max_length=200)    
    sol_estado: str = Field(min_length=5, max_length=50)  
    pet_id: str = Field()  

    class Config:
        schema_extra = {
            "example": {                                
                "sol_descripcion": "sol_descripcion",
                "sol_estado": "sol_estado",
                "pet_id": 0
            }
        }
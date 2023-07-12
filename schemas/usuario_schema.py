from typing import Optional
from pydantic import BaseModel, Field

class Usuario(BaseModel):
    
    usr_username: str = Field(max_length=50)
    usr_password: str = Field(max_length=50)
    repeat_password: str = Field(max_length=50)
    per_id: int = Field()    

    class Config:
        schema_extra = {
            "example": {                                
                "usr_username": "username",
                "usr_password": "123456",
                "repeat_password": "123456",
                "per_id": 0,                
            }
        }

class UsuarioLogin(BaseModel):

    username: str = Field(max_length=50)
    password: str = Field(max_length=50)


    class Config:
        schema_extra = {
            "example": {                                
                "username": "username",
                "password": "123456",             
            }
        }
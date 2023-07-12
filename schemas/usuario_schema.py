from typing import Optional
from pydantic import BaseModel, Field

class Usuario(BaseModel):
    
    usr_username: str = Field(max_length=50)
    usr_password: str = Field(max_length=50)
    repeat_password: str = Field(max_length=50)
    identificacion: str = Field(max_length=15)    

    class Config:
        schema_extra = {
            "example": {                                
                "usr_username": "username",
                "usr_password": "123456",
                "repeat_password": "123456",
                "identificacion": "1234567890",                
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
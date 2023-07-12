from models.usuario import Usuario as UsuarioModel
from schemas.usuario_schema import Usuario, UsuarioLogin
from datetime import datetime, timedelta
from jose import JWTError, jwt
from config.config import SECRET_KEY, ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES = 60

class AuthService():

    def __init__(self, db) -> None:
        self.db = db    

    def register(self, usuario: Usuario):
        new_usuario = UsuarioModel().save_user(usuario.dict())
        self.db.add(new_usuario)
        self.db.commit()
        return usuario.dict()
    
    def login(self, usuario: UsuarioLogin):
        user = self.db.query(UsuarioModel).filter(UsuarioModel.usr_username == usuario.dict()['username']).first()
        if user:
            clave = user.check_password(usuario.dict()['password'])
            if user and clave:
                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)                
                access_token = create_token(data={'user': user.usr_username, 'per': user.per_id}, expires_delta=access_token_expires)
                return access_token

        return {"msg": "El usuario o contraseña son incorrectos."}
    
    
def create_token(data: dict, expires_delta: timedelta):    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    # to_encode.update({'exp': expire})    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
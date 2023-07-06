from models.usuario import Usuario as UsuarioModel
from schemas.usuario_schema import Usuario, UsuarioLogin


class AuthService():

    def __init__(self, db) -> None:
        self.db = db

    def register(self, usuario: Usuario):
        new_usuario = UsuarioModel().save_user(usuario.dict())
        self.db.add(new_usuario)
        self.db.commit()
        return usuario.dict()
    
    def login(self, usuario: UsuarioLogin):
        user = self.db.query(UsuarioModel).filter(UsuarioModel.usr_username == usuario.dict()['usr_username']).first()
        clave = user.check_password(usuario.dict()['usr_password'])
        if user:
            if user and clave:
                return "LOGIN"
        return "El usuario o contraseña son incorrectos."
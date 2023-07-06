from models.usuario import Usuario as UsuarioModel

class UsuarioService():

    def __init__(self, db) -> None:
        self.db = db

    def get_usuarios(self):
        return self.db.query(UsuarioModel).all()    
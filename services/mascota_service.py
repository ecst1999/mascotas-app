from models.mascota import Mascota as MascotaModel

class MascotaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_mascotas(self):
        result = self.db.query(MascotaModel).all()
        return result
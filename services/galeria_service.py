from models.galeria import Galeria as GaleriaModel

class GaleriaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_galerias(self):
        result = self.db.query(GaleriaModel).all()
        return result
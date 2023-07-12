from models.galeria import Galeria as GaleriaModel
from schemas.galeria_schema import Galeria

class GaleriaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_galerias(self):
        result = self.db.query(GaleriaModel).filter(GaleriaModel.gal_estado == True).all()
        return result
    
    def add_galeria(self, galeria: Galeria):
        new_galeria = GaleriaModel(**galeria.dict())
        self.db.add(new_galeria)
        self.db.commit()
        return
    
    def get_galeria(self, id: int):
        return self.db.query(GaleriaModel).filter(GaleriaModel.gal_estado == True, GaleriaModel.gal_id == id).first()
    
    def update_galeria(self, id: int, data: Galeria):
        galeria = self.db.query(GaleriaModel).filter(GaleriaModel.gal_estado == True, GaleriaModel.gal_id == id).first()

        galeria.gal_nombre = data.gal_nombre
        galeria.gal_pathImagen = data.gal_pathImagen
        
        self.db.commit()
        return
    
    def delete_galeria(self, id: int):
        galeria = self.db.query(GaleriaModel).filter(GaleriaModel.gal_estado == True, GaleriaModel.gal_id == id).first()
        galeria.gal_estado = False
        self.db.commit()
        return
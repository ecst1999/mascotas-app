from models.galeria import Galeria as GaleriaModel
from schemas.galeria_schema import Galeria

class GaleriaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_galerias(self):
        result = self.db.query(GaleriaModel).filter(GaleriaModel.gal_estado == True).all()
        return result
    
    def add_galeria(self, galeria_nombre: str, galeria_path: str, pet: int):
        new_galeria = GaleriaModel(gal_nombre=galeria_nombre, gal_pathImagen=galeria_path, pet_id = pet)
        self.db.add(new_galeria)
        self.db.commit()
        return
    
    def get_galeria(self, id: int):
        return self.db.query(GaleriaModel).filter(GaleriaModel.gal_estado == True, GaleriaModel.gal_id == id).first()
    
    def update_galeria(self, id: int, nombreGaleria: str, gal_pathImagen: str):
        galeria = self.db.query(GaleriaModel).filter(GaleriaModel.gal_estado == True, GaleriaModel.gal_id == id).first()

        galeria.gal_nombre = nombreGaleria
        galeria.gal_pathImagen = gal_pathImagen
        
        self.db.commit()
        return
    
    def delete_galeria(self, id: int):
        galeria = self.db.query(GaleriaModel).filter(GaleriaModel.gal_estado == True, GaleriaModel.gal_id == id).first()
        galeria.gal_estado = False
        self.db.commit()
        return
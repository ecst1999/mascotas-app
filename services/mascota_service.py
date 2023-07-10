from models.mascota import Mascota as MascotaModel
from schemas.mascota_schema import Mascota

class MascotaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_mascotas(self):
        result = self.db.query(MascotaModel).filter(MascotaModel.pet_estado == True).all()
        return result
    
    def add_mascota(self, mascota: Mascota):
        new_mascota = MascotaModel(**mascota.dict())
        self.db.add(new_mascota)
        self.db.commit()
        return
    
    def get_mascota(self, id: int):
        result = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True).first()
        return result
    
    def update_mascota(self, id: int, data: Mascota):
        
        mascota = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True).first()

        mascota.pet_nombre = data.pet_nombre
        mascota.pet_nombre = data.pet_nombre
        mascota.pet_especie = data.pet_especie
        mascota.pet_edad = data.pet_edad

        self.db.commit()
        return
    
    def delete_mascota(self, id: int):

        mascota = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True).first()

        mascota.pet_estado = False

        self.db.commit()

        return
from models.mascota import Mascota as MascotaModel
from schemas.mascota_schema import Mascota

class MascotaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_mascotas(self):
        result = self.db.query(MascotaModel).filter(MascotaModel.pet_estado == True).all()
        return result
    
    def get_mascotas_personas(self, persona: int):
        return self.db.query(MascotaModel).filter(MascotaModel.pet_estado == True, MascotaModel.per_id == persona).all()
    
    def add_mascota(self, mascota: Mascota, persona: int):
        new_mascota = MascotaModel(**mascota.dict(), per_id = persona)
        self.db.add(new_mascota)
        self.db.commit()
        return
    
    def get_mascota(self, id: int):
        result = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True).first()
        return result
    
    def update_mascota(self, id: int, data: Mascota, persona: int):
        
        mascota = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True, MascotaModel.per_id == persona).first()
        
        mascota.pet_nombre = data.pet_nombre
        mascota.pet_especie = data.pet_especie
        mascota.pet_edad = data.pet_edad

        self.db.commit()
        return
    
    def delete_mascota(self, id: int, persona: int):

        mascota = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True, MascotaModel.per_id == persona).first()
        mascota.pet_estado = False

        self.db.commit()
        return
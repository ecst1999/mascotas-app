from models.mascota import Mascota as MascotaModel
from schemas.mascota_schema import Mascota
from models.galeria import Galeria

class MascotaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_mascotas(self):
        result = self.db.query(MascotaModel).filter(MascotaModel.pet_estado == True).all()
        if result:
            for row in result:
                print(row.galerias)
        return result
    
    def get_mascotas_personas(self, persona: int):
        result = self.db.query(MascotaModel).filter(MascotaModel.pet_estado == True, MascotaModel.per_id == persona).all()
        if result: 
            for row in result:
                print(row.galerias)
        return result
    
    def add_mascota(self, mascota: dict, persona: int):
        new_mascota = MascotaModel(**mascota, per_id = persona)
        self.db.add(new_mascota)
        self.db.commit()
        return
    
    def get_mascota(self, id: int):
        result = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True).first()        
        if result:
            for row in result.galerias:
                print(row)
        return result
    
    def update_mascota(self, id: int, data: dict, persona: int):
        
        mascota = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True, MascotaModel.per_id == persona).first()
        
        mascota.pet_nombre = data['pet_nombre']
        mascota.pet_especie = data['pet_especie']
        mascota.pet_edad = data['pet_edad']
        mascota.pet_foto_perfil = data['pet_foto_perfil']

        self.db.commit()
        return mascota
    
    def delete_mascota(self, id: int, persona: int):

        mascota = self.db.query(MascotaModel).filter(MascotaModel.pet_id == id, MascotaModel.pet_estado == True, MascotaModel.per_id == persona).first()
        mascota.pet_estado = False

        self.db.commit()
        return
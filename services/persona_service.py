from models.persona import Persona as PersonaModel
from schemas.persona_schema import Persona


class PersonaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_personas(self):
        return self.db.query(PersonaModel).filter(PersonaModel.per_estado == True).all()        
    
    def get_persona(self, id):
        return self.db.query(PersonaModel).filter(PersonaModel.per_id == id, PersonaModel.per_estado == True).first()
    
    def update_persona(self, data: Persona, per: int):
        persona = self.db.query(PersonaModel).filter(PersonaModel.per_estado == True, PersonaModel.per_id == per).first()        
        
        persona.per_nombre = data.per_nombre
        persona.per_apellido = data.per_apellido
        persona.per_telefono = data.per_telefono
        persona.per_correo = data.per_correo
        persona.per_completo = True
        persona.per_direccion = data.per_direccion
        persona.per_foto_documento = "foto"                                   

        self.db.commit()
        return
    
    def delete_persona(self, id:int):
        persona = self.db.query(PersonaModel).filter(PersonaModel.per_id == id).first()
        persona.per_estado = False
        self.db.commit()
        return

    def activar_cuenta(self, id:int):
        persona = self.db.query(PersonaModel).filter(PersonaModel.per_id == id).first()
        persona.per_esta_activo = True
        self.db.commit()
        return
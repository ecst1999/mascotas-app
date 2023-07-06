from models.persona import Persona as PersonaModel
from schemas.persona_schema import Persona

class PersonaService():

    def __init__(self, db) -> None:
        self.db = db

    def get_personas(self):
        return self.db.query(PersonaModel).all()    
    
    def add_personas(self, persona: Persona):
        new_persona = PersonaModel(**persona.dict())
        self.db.add(new_persona)
        self.db.commit()
        return
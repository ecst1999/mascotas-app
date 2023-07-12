from models.solicitud import Solicitud as SolicitudModel
from schemas.solicitud_schema import Solicitud

class SolicitudService():

    def __init__(self, db) -> None:
        self.db = db

    def get_solicitudes(self, persona: int):
        return self.db.query(SolicitudModel).filter(SolicitudModel.per_id == persona).all()
    
    def add_solicitud(self, solicitud: Solicitud, persona: int):
        new_solicitud = SolicitudModel(**solicitud.dict(), per_id = persona)
        self.db.add(new_solicitud)
        self.db.commit()
        return
    
    def get_solicitud(self, id: int, persona: int):
        return self.db.query(SolicitudModel).filter(SolicitudModel.sol_id == id, SolicitudModel.per_id == persona).first()
    
    def update_solicitud(self, id: int, data: Solicitud, persona: int):
        solicitud = self.db.query(SolicitudModel).filter(SolicitudModel.sol_id == id, SolicitudModel.per_id == persona).first()

        solicitud.sol_descripcion = data.sol_descripcion
        solicitud.sol_estado = data.sol_estado

        self.db.commit()
        return
    
    def delete_solicitud(self, id: int, persona: int):
        self.db.query(SolicitudModel).filter(SolicitudModel.sol_id == id, SolicitudModel.per_id == persona).delete()
        self.db.commit()
        return



from models.solicitud import Solicitud as SolicitudModel

class SolicitudService():

    def __init__(self, db) -> None:
        self.db = db

    def get_solicitudes(self):
        return self.db.query(SolicitudModel).all()
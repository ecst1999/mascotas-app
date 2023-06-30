from config.database import Base
from sqlalchemy import Column, Integer, String

class Solicitud(Base):

    __tablename__ = "solicitudes"

    id = Column(Integer, primary_key=True)
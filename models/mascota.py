from config.database import Base
from sqlalchemy import Column, Integer, String

class Mascota(Base):

    __tablename__ = "mascotas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    especie = Column(String(100))
    edad = Column(Integer)
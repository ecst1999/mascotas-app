from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship

class Mascota(Base):

    __tablename__ = "mascotas"

    pet_id = Column(Integer, primary_key=True, autoincrement=True)
    pet_nombre = Column(String(100))
    pet_especie = Column(String(100))
    pet_edad = Column(Integer)    
    pet_foto_perfil = Column(Text)
    pet_estado = Column(Boolean, default=True)

    per_id = Column(Integer, ForeignKey("personas.per_id"))

    galerias = relationship("Galeria" ,back_populates="mascotas")
    personas = relationship("Persona", back_populates="mascotas")
    solicitudes = relationship("Solicitud", back_populates="mascotas")
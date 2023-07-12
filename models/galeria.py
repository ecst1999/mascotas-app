from config.database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Galeria(Base):

    __tablename__ = "galerias"

    gal_id = Column(Integer, primary_key=True, autoincrement=True)
    gal_nombre = Column(String(100))
    gal_pathImagen = Column(Text)
    gal_estado = Column(Boolean, default=True)

    pet_id = Column(Integer, ForeignKey('mascotas.pet_id'))
    mascotas = relationship("Mascota", back_populates="galerias")
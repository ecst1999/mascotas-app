from config.database import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

class Persona(Base):

    __tablename__ = "personas"

    per_id = Column(Integer, primary_key=True, autoincrement=True)
    per_identificacion = Column(String(20), unique=True, nullable=False)
    per_nombre = Column(String(100))
    per_apellido = Column(String(100))
    per_telefono = Column(String(15))
    per_correo = Column(String(75))
    per_direccion = Column(Text)

    # solicitudes = relationship("Solicitud", back_populates="personas")
    # mascotas = relationship("Mascota", back_populates="personas")
    usuarios = relationship("Usuario", back_populates="personas")
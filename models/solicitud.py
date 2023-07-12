import datetime
from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

class Solicitud(Base):

    __tablename__ = "solicitudes"

    sol_id = Column(Integer, primary_key=True, autoincrement=True)
    sol_fecha = Column(DateTime, default=datetime.datetime.utcnow)
    sol_descripcion = Column(Text)
    sol_estado = Column(String(50))

    per_id = Column(Integer, ForeignKey("personas.per_id"))
    # persona = relationship("Persona", back_populates="solicitudes")

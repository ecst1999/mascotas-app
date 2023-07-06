from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Role(Base):

    __tablename__ = "roles"

    rol_id = Column(Integer, primary_key=True)
    rol_nombre = Column(String(50))

    usuarios = relationship("Usuario", back_populates="roles")
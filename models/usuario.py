from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from models.role import Role

class Usuario(Base):

    __tablename__ = "usuarios"

    usr_id = Column(Integer, primary_key=True, autoincrement=True)
    usr_username = Column(String(50), unique=True, nullable=False)
    usr_password = Column(Text)
    usr_estado = Column(Boolean, default=True)

    per_id = Column(Integer, ForeignKey("personas.per_id"))
    rol_id = Column(Integer, ForeignKey("roles.rol_id"), default=2)

    personas = relationship("Persona", back_populates="usuarios")
    roles = relationship("Role", back_populates="usuarios")

    def set_password(self, password):
        self.usr_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.usr_password, password)
    
    def save_user(self, usuario: dict):
        self.usr_username = usuario['usr_username']
        self.set_password(usuario['usr_password'])
        self.per_id = usuario['per_id']

        return self

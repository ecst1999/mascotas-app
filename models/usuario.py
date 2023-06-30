from config.database import Base
from sqlalchemy import Column, Integer, String

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
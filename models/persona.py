from config.database import Base
from sqlalchemy import Column, Integer, String

class Persona(Base):

    __tablename__ = "personas"

    id = Column(Integer, primary_key=True)
from config.database import Base
from sqlalchemy import Column, Integer, String

class Rol(Base):

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
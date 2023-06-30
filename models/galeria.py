from config.database import Base
from sqlalchemy import Column, Integer, String

class Galeria(Base):

    __tablename__ = "galerias"

    id = Column(Integer, primary_key=True)
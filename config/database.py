from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://api:12345@localhost:3307/api?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
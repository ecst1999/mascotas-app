from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://api:12345@localhost:3307/api?charset=utf8mb4", echo=True)
# engine = create_engine("postgresql://mascotas_app_user:vUepE4OVRSkA3wUYRjWeU5PXDc71rjVe@dpg-cio8hnp8g3n6h7j709t0-a/mascotas_app", echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
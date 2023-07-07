from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql+pg8000://api:2eGt8yXoPI94AkN1QsMFI4iCgkjUs97R@dpg-cik2b7unqql0l1v86i20-a/api_v9fb", echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
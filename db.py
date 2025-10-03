from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

data_base = create_engine("sqlite:///banco.db")
Session= sessionmaker(bind=data_base)

Base = declarative_base()
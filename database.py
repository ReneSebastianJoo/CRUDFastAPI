import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_DIALECT = os.getenv("DB_DIALECT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")


URL_DATABASE = "{}://{}:{}@{}/{}".format(DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

engine = create_engine(URL_DATABASE)

conn = engine.connect()

meta = MetaData()

sessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()
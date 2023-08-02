from sqlalchemy import Table, Column, Integer, String, Boolean
from database import meta, sessionLocal, engine
from database import Base

users = Table("users", meta,
              Column("id", Integer, primary_key=True),
              Column("name", String(50), nullable=False),
              Column("email", String(150), nullable=False),
              Column("password", String(50), nullable=False)
              )

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name =Column(String(50))
    email =Column(String(150), unique=True)
    password =Column(String(50))


meta.create_all(engine)
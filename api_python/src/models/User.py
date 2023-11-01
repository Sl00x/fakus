from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

from database import engine

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)


# Create the table on DB automatically, when this class is loaded
Base.metadata.create_all(bind=engine)

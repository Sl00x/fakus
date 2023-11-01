from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config import Config

SQLALCHEMY_DATABASE_URL = Config.read('app', 'db.url')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    db_session: Session = session()
    try:
        yield db_session
    finally:
        db_session.close()

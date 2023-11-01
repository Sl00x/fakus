from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db_session

from ..models.User import User


class SampleRepository():
    def __init__(self, db_session: Session = Depends(get_db_session)) -> None:
        self.db = db_session

    def find(self):

        return self.db.query(User).get()

    def insert(self, item):
        db_item = User(id=item.id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)

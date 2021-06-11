from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String, Text
from datetime import datetime as dt
from database import Database


class Entry(Database.create_base()):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(String(300), nullable=True)
    content = Column(Text, nullable=False)
    date = Column(DateTime, default=dt.utcnow)

    def __repr__(self):
        return f"ID: {self.id}, title: {self.title}, desc: {self.description}"




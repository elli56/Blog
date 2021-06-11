from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    @classmethod
    def __create_engine(cls):
        cls.engine = create_engine("postgresql+psycopg2://ildar:1234@localhost:5432/sqlalchemy2", echo=False)
        return cls.engine

    @classmethod
    def __create_all(cls):
        cls.Base.metadata.create_all(cls.engine)

    @classmethod
    def __create_session(cls):
        Session = sessionmaker()
        Session.configure(bind=cls.engine)
        session = Session()
        return session

    @classmethod
    def create_base(cls):
        cls.Base = declarative_base()
        return cls.Base

    @staticmethod
    def database_launch():
        Database.__create_engine()
        Database.__create_all()
        session = Database.__create_session()
        return session

























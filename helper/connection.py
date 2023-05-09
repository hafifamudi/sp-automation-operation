from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

class Connection(object):

    def __init__(self, db_connection):
        engine = create_engine(db_connection, future=True)
        self.engine = engine
        
    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def get_engine(self):
        return self.engine

    def test_engine(self):
        self.engine.connect()

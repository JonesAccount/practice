from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

Base.metadata.create_all(engine)
from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///iftar.db')

Base = declarative_base()
 
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    city = Column(String)

    def __repr__(self):
        return f'User(id={self.id}, full_name="{self.full_name}", city="{self.city}")' 
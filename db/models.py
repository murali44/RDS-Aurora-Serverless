import enum
import sys

from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User():
    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True)
    email = Column('email', VARCHAR(128))
    date_joined = Column('date_joined', DateTime(timezone=True))
    first_name = Column('first_name', VARCHAR(50))
    last_name = Column('last_name', VARCHAR(100))

# Create Tables
def create_tables(engine):
    print("****** Creating/Updating Tables ******")
    Base.metadata.create_all(bind=engine)

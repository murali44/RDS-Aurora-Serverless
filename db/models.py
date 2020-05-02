import enum
import sys

from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy import Integer, BigInteger, Text, Float
from sqlalchemy import VARCHAR, Enum, Boolean, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

sys.path.append('..')

from src.utils import ModelMixin

Base = declarative_base()

class User(Base, ModelMixin):
    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True)
    cognito_id = Column('cognito_id', VARCHAR(50), nullable=False, unique=True)
    email = Column('email', VARCHAR(128), nullable=False, unique=True)
    is_superuser = Column('is_superuser', Boolean, nullable=False)
    is_staff = Column('is_staff', Boolean, nullable=False)
    date_joined = Column('date_joined', DateTime(timezone=True), nullable=False)
    last_login = Column('last_login', DateTime(timezone=True), nullable=False)

    first_name = Column('first_name', VARCHAR(50), nullable=True)
    last_name = Column('last_name', VARCHAR(100), nullable=True)

    groups = relationship('Group', secondary='user_group', backref='users')
    permissions = relationship('Permission', secondary='user_permission', backref='users')

    def toJSON(self):
        return dict(id=self.id,
                    cognito_id=self.cognito_id,
                    first_name=self.first_name,
                    last_name=self.last_name,
                    email=self.email,
                    is_superuser=self.is_superuser,
                    is_staff=self.is_staff,
                    date_joined=self.date_joined.isoformat() if self.date_joined else None,
                    last_login=self.last_login.isoformat() if self.last_login else None,
                    permissions=[p.id for p in self.permissions],
                    groups=[g.id for g in self.groups]
                    )

# Create Tables
def create_tables(engine):
    print("****** Creating/Updating Tables ******")
    Base.metadata.create_all(bind=engine)

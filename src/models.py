import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    address = Column(String(250), nullable=True)
    phone_number = Column(String(30), nullable=False)
    creation_date = Column(String(30), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table planets
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    region = Column(String(30), nullable=False)
    sector = Column(String(30), nullable=False)
    system = Column(String(30), nullable=False)
    inhabitans = Column(Integer, nullable=False)
    capital = Column(String(30), nullable=False)
    population = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    atmosphere = Column(String(30), nullable=False)
    language = Column(String(30), nullable=False)
    affiliation = Column(String(30), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table character
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    homeworld = Column(String(30), nullable=False)
    born = Column(String(30), nullable=False)
    died = Column(String(30), nullable=True)
    gender = Column(String(30), nullable=False)
    affiliation = Column(String(30), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table character
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)


    def to_dict(self):
        return {}

    def login(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
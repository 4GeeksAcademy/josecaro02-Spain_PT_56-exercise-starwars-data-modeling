import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Country(Base):
    __tablename__= 'country'
    ID = Column(Integer, primary_key=True)
    name =Column(String(10))

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    pais = Column(Integer, ForeignKey('country.ID'))
    pais_relationship = relationship(Country)
    email = Column(String(50), unique=True)
    password = Column(String(25))

class Character(Base):
    __tablename__ = 'character'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    height = Column(Integer)
    mass = Column(Integer)

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    user_relationship = relationship(User)
    character_id = Column(Integer, ForeignKey('character.ID'))
    character_relationship = relationship(Character)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

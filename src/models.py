import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True)
    email = Column(String(250), unique=True)
    password_hash = Column(String(250))
    favorites = relationship("Favorite", back_populates="user")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer)
    # Add other planet properties here

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    species = Column(String(250))
    gender = Column(String(250))
    # Add other character properties here

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet")
    character = relationship("Character")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

#!/usr/bin/python3
# OOP and sql first task
# using sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

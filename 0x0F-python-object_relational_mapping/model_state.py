#!/usr/bin/env python
"""
Defines State class inheriting from Base, links to MySQL table 'states'.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


eng = create_engine('mysql://username:password@localhost:3306/database_name')

Base = declarative_base()


class State(Base):
    """Class att: 'id' as an auto-generated unique integer (primary key)"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(eng)

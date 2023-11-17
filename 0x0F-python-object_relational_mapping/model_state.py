#!/usr/bin/env python3
"""
Defines a State class and creates a corresponding MySQL table using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the 'states' table in MySQL.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://username:password@localhost:3306/database_name', echo=True
    )
    Base.metadata.create_all(engine)

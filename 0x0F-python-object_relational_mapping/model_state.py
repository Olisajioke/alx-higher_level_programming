#!/usr/bin/python3
"""module that starts the link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    db_connection_string = (
        'mysql+mysqldb://{}:{}@localhost/{}'
    ).format(db_user, db_password, db_name)

    my_engine = create_engine(db_connection_string, pool_pre_ping=True)
    Base.metadata.create_all(my_engine)

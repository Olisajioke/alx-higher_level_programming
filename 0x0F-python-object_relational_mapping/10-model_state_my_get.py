#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    my_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(my_engine)
    MySession = sessionmaker(bind=my_engine)
    my_session = MySession()
    my_instance = my_session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(my_instance[0].id)
    except IndexError:
        print("Not found")

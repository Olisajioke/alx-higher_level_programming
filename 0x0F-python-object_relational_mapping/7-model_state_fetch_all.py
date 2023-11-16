#!/usr/bin/python3
"""Start link class to table in database"""
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
    for instance in my_session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")

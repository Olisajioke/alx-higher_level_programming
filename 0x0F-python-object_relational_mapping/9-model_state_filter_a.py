#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa"""
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
    for sess in my_session.query(State).filter(State.name.like('%a%')):
        print(sess.id, sess.name, sep=": ")

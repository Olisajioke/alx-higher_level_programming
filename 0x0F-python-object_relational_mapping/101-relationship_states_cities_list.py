#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    my_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(my_engine)
    MySession = sessionmaker(bind=my_engine)
    my_session = MySession()
    for my_instance in my_session.query(State).order_by(State.id):
        print(my_instance.id, my_instance.name, sep=": ")
        for city_ins in my_instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")

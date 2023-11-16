#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    my_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                              format(sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)
    Base.metadata.create_all(my_engine)

    MySession = sessionmaker(bind=my_engine)
    my_session = MySession()

    my_state = State(name='California')
    my_city = City(name='San Francisco')
    my_state.cities.append(my_city)

    my_session.add(my_state)
    my_session.add(my_city)
    my_session.commit()

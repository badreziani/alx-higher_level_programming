#!/usr/bin/python3
"""7-model_state_fetch_all
lists all State objects from the database hbtn_0e_6_usa
using the SQLAlchemy module
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    [print(f"{state.id}: {state.name}") for state in states]

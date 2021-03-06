#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)()
    new_state = State(name="Louisiana")
    Session.add(new_state)
    Session.commit()
    state_rows = Session.query(State).order_by(State.id)
    for item in state_rows:
        new_id = item.id
    print(str(new_id))

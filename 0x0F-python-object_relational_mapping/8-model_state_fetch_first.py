#!/usr/bin/python3
"""
    get all states
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://" + sys.argv[1] +
        ":" + sys.argv[2] +
        "@localhost/" + sys.argv[3],
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    w = session.query(State).order_by(State.id).first()
    if w:
        print(str(w.id) + ": " + str(w.name))
    else:
        print("Nothing")
    session.close()

#!/usr/bin/python3
# fetchall sqlalchemy
if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{\
}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker()
    session = session(bind=engine)
    ses = session.query(State).filter(State.name.contains('a'))
    for ele in ses:
        print("{}: {}".format(ele.id, ele.name))

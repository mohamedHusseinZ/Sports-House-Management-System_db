
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///sports_house.db')
Base = declarative_base()

class Athlete(Base):
    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    contact_info = Column(String)
    sports_specialty = Column(String)
    unique_identifier = Column(String)

    # one-to-many relationship with Result
    results = relationship('Result', back_populates='athlete')

    def __repr__(self):
        return f'<Athlete(id={self.id}, name={self.name}, age={self.age}, sports_specialty={self.sports_specialty}, unique_identifier={self.unique_identifier})>'

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime)
    time = Column(DateTime)
    location = Column(String)

    #  a many-to-one relationship with Result
    results = relationship('Result', back_populates='event')

    def __repr__(self):
        return f'<Event(id={self.id}, name={self.name}, date={self.date}, time={self.time}, location={self.location})>'

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    result_value = Column(String)
    athlete_id = Column(Integer, ForeignKey('athletes.id'))
    event_id = Column(Integer, ForeignKey('events.id'))

    athlete = relationship('Athlete', back_populates='results')
    event = relationship('Event', back_populates='results')

    def __repr__(self):
        return f'<Result(id={self.id}, result_value={self.result_value}, athlete_id={self.athlete_id}, event_id={self.event_id})>'

#  the tables in the database
Base.metadata.create_all(engine)

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()

    # add data 
    athlete1 = Athlete(name="zaki hussen", age=25, sports_specialty="Swimming", unique_identifier="JD123")
    athlete2 = Athlete(name="mo farah", age=30, sports_specialty="Running", unique_identifier="JS456")

    event1 = Event(name="Swimming Competition", date=datetime.now(), time=datetime.now(), location="Pool")
    event2 = Event(name="Running Race", date=datetime.now(), time=datetime.now(), location="Track")

    result1 = Result(result_value="1st Place", athlete=athlete1, event=event1)
    result2 = Result(result_value="2nd Place", athlete=athlete2, event=event1)
    result3 = Result(result_value="3rd Place", athlete=athlete1, event=event2)

    # Add the objects to the session
    session.add_all([athlete1, athlete2, event1, event2, result1, result2, result3])

    print("\nQuerying and printing added data:")
    athletes = session.query(Athlete).all()
    for athlete in athletes:
        print(athlete)

    events = session.query(Event).all()
    for event in events:
        print(event)

    results = session.query(Result).all()
    for result in results:
        print(result)

    session.commit()
    session.close()


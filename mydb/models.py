from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime

# Initialize the database engine and Base class
engine = create_engine('sqlite:///sports_house.db')
Base = declarative_base()

# Define the Athlete model
class Athlete(Base):
    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    contact_info = Column(String)
    sports_specialty = Column(String)
    unique_identifier = Column(String)

    # One-to-many relationship with Result
    results = relationship('Result', back_populates='athlete')

    def __repr__(self):
        return f'<Athlete(id={self.id}, name={self.name}, age={self.age}, sports_specialty={self.sports_specialty}, unique_identifier={self.unique_identifier})>'

# Define the Event model
class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime)
    time = Column(DateTime)
    location = Column(String)

    # One-to-many relationship with Result
    results = relationship('Result', back_populates='event')

    def __repr__(self):
        return f'<Event(id={self.id}, name={self.name}, date={self.date}, time={self.time}, location={self.location})>'

# Define the Result model
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

# Create the tables in the database
Base.metadata.create_all(engine)

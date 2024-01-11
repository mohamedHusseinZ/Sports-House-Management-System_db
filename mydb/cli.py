import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Athlete, Event, Result
from datetime import datetime  # Add this import for the datetime object

engine = create_engine('sqlite:///sports_house.db')
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
def view_athletes():
    athlete_name = click.prompt('Enter athlete name')
    session = Session()
    athletes = session.query(Athlete).filter(Athlete.name == athlete_name).all()
    for athlete in athletes:
        print(athlete)
    session.close()

@cli.command()
def view_events():
    session = Session()
    events = session.query(Event).all()
    for event in events:
        print(event)
    session.close()

@cli.command()
def view_results():
    athlete_name = click.prompt('Enter athlete name')
    session = Session()
    results = session.query(Result).join(Athlete).filter(Athlete.name == athlete_name).all()
    for result in results:
        print(result)
    session.close()

@cli.command()
def add_data():
    session = Session()

    # Input data for Athlete
    athlete_name = click.prompt('Enter athlete name')
    athlete_age = click.prompt('Enter athlete age', type=int)
    sports_specialty = click.prompt('Enter sports specialty')
    unique_identifier = click.prompt('Enter unique identifier')

    athlete = Athlete(name=athlete_name, age=athlete_age, sports_specialty=sports_specialty, unique_identifier=unique_identifier)
    session.add(athlete)

    # Input data for Event
    event_name = click.prompt('Enter event name')
    event_date = click.prompt('Enter event date (YYYY-MM-DD)', type=click.DateTime(formats=["%Y-%m-%d"]))
    event_time = click.prompt('Enter event time (HH:MM)', type=click.DateTime(formats=["%H:%M"]))
    event_location = click.prompt('Enter event location')

    event = Event(name=event_name, date=event_date, time=event_time, location=event_location)
    session.add(event)

    # Input data for Result
    result_value = click.prompt('Enter result value')
    event_id = click.prompt('Enter event ID for the result', type=int)
    athlete_id = click.prompt('Enter athlete ID for the result', type=int)

    result = Result(result_value=result_value, athlete_id=athlete_id, event_id=event_id)
    session.add(result)

    session.commit()
    session.close()

if __name__ == '__main__':
    cli()


from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from models import Athlete, Event, Result

#  a Faker instance
fake = Faker()

engine = create_engine('sqlite:///sports_house.db')
Session = sessionmaker(bind=engine)
session = Session()

# Sample data
athletes_data = [
    {"name": fake.name(), "age": fake.random_int(min=18, max=40), "sports_specialty": "Swimming", "unique_identifier": fake.uuid4()},
    {"name": fake.name(), "age": fake.random_int(min=18, max=40), "sports_specialty": "Running", "unique_identifier": fake.uuid4()},
]

events_data = [
    {"name": "Swimming Competition", "date": fake.date_between(start_date='-30d', end_date='today'), "time": fake.time(), "location": "Pool"},
    {"name": "Running Race", "date": fake.date_between(start_date='-30d', end_date='today'), "time": fake.time(), "location": "Track"},
]

results_data = [
    {"result_value": "1st Place"},
    {"result_value": "2nd Place"},
    {"result_value": "3rd Place"},
]

#  Athlete objects
athletes = [Athlete(**data) for data in athletes_data]

#  Event objects
events = [Event(**data) for data in events_data]

#  Result objects
results = [Result(result_value=data["result_value"]) for data in results_data]

# Assign athletes and events to results
results[0].athlete, results[0].event = athletes[0], events[0]
results[1].athlete, results[1].event = athletes[1], events[0]
results[2].athlete, results[2].event = athletes[0], events[1]

# Add objects to the session
session.add_all(athletes + events + results)


# Commit and close the session
session.commit()
session.close()




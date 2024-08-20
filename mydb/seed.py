from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Athlete, Event, Result
from datetime import datetime

# Initialize the database engine and sessionmaker
engine = create_engine('sqlite:///sports_house.db')
Session = sessionmaker(bind=engine)

# Seed the database with initial data
def seed_data():
    session = Session()

    # Create athletes
    athlete1 = Athlete(name="Zaki Hussen", age=25, contact_info="zaki@example.com", sports_specialty="Swimming", unique_identifier="JD123")
    athlete2 = Athlete(name="Mo Farah", age=30, contact_info="mo@example.com", sports_specialty="Running", unique_identifier="JS456")

    # Create events
    event1 = Event(name="Swimming Competition", date=datetime.now(), time=datetime.now(), location="Pool")
    event2 = Event(name="Running Race", date=datetime.now(), time=datetime.now(), location="Track")

    # Create results
    result1 = Result(result_value="1st Place", athlete=athlete1, event=event1)
    result2 = Result(result_value="2nd Place", athlete=athlete2, event=event1)
    result3 = Result(result_value="3rd Place", athlete=athlete1, event=event2)

    # Add the objects to the session
    session.add_all([athlete1, athlete2, event1, event2, result1, result2, result3])

    # Commit and close the session
    session.commit()
    session.close()
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()

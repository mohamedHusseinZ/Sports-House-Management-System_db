from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Athlete, Event, Result, Base  # Assuming your SQLAlchemy models are in a separate `models.py` file
from datetime import datetime

app = Flask(__name__)

# Setup the database connection
engine = create_engine('sqlite:///sports_house.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@app.route('/athletes', methods=['GET'])
def get_athletes():
    session = Session()
    athletes = session.query(Athlete).all()
    session.close()
    return jsonify([{
        'id': athlete.id,
        'name': athlete.name,
        'age': athlete.age,
        'contact_info': athlete.contact_info,
        'sports_specialty': athlete.sports_specialty,
        'unique_identifier': athlete.unique_identifier
    } for athlete in athletes])

@app.route('/athletes/<int:id>', methods=['GET'])
def get_athlete(id):
    session = Session()
    athlete = session.query(Athlete).get(id)
    session.close()
    if athlete:
        return jsonify({
            'id': athlete.id,
            'name': athlete.name,
            'age': athlete.age,
            'contact_info': athlete.contact_info,
            'sports_specialty': athlete.sports_specialty,
            'unique_identifier': athlete.unique_identifier
        })
    else:
        return jsonify({'error': 'Athlete not found'}), 404

@app.route('/athletes', methods=['POST'])
def add_athlete():
    data = request.get_json()
    session = Session()
    new_athlete = Athlete(
        name=data['name'],
        age=data['age'],
        contact_info=data.get('contact_info', ''),
        sports_specialty=data['sports_specialty'],
        unique_identifier=data['unique_identifier']
    )
    session.add(new_athlete)
    session.commit()
    session.close()
    return jsonify({'message': 'Athlete added successfully'}), 201

@app.route('/events', methods=['GET'])
def get_events():
    session = Session()
    events = session.query(Event).all()
    session.close()
    return jsonify([{
        'id': event.id,
        'name': event.name,
        'date': event.date,
        'time': event.time,
        'location': event.location
    } for event in events])

@app.route('/results', methods=['GET'])
def get_results():
    session = Session()
    results = session.query(Result).all()
    session.close()
    return jsonify([{
        'id': result.id,
        'result_value': result.result_value,
        'athlete_id': result.athlete_id,
        'event_id': result.event_id
    } for result in results])

@app.route('/results', methods=['POST'])
def add_result():
    data = request.get_json()
    session = Session()
    new_result = Result(
        result_value=data['result_value'],
        athlete_id=data['athlete_id'],
        event_id=data['event_id']
    )
    session.add(new_result)
    session.commit()
    session.close()
    return jsonify({'message': 'Result added successfully'}), 201


if __name__ == '__main__':

    app.run(debug=True, port=8000)


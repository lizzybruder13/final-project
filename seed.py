

from sqlalchemy import func
from model import connect_to_db, db, Event, Location, Event_Type
from datetime import datetime
from server import app


def load_event_types():
    """Load events types from event_type_data.txt to database."""

    print("Loading Event Types...")

    Event_Type.query.delete()

    for row in open("static/event_type_data.txt"):
        row = row.rstrip()
        type_name = row

        event_type = Event_Type(type_name=type_name)

        db.session.add(event_type)

    db.session.commit()


def load_locations():
    """Load locations from location_data.txt to database."""

    print("Loading Locations...")

    Location.query.delete()

    for row in open("static/location_data.txt"):
        row = row.rstrip()
        name, address, city, zipcode = row.split(" | ")

        location = Location(name=name, address=address, 
                            city=city, zipcode=zipcode)

        db.session.add(location)

    db.session.commit()


def load_events():
    """Load events from event_data.txt to database."""

    print("Loading Events...")

    Event.query.delete()

    for row in open("static/event_data.txt"):
        row = row.rstrip()
        location_id, type_id, time, weekday = row.split(" | ")

        event = Event(location_id=location_id, type_id=type_id, 
                      time=time, weekday=weekday)

        db.session.add(event)

    db.session.commit() 


if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()

    
    load_event_types()
    load_locations()
    load_events()




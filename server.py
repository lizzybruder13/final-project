

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Event, Location, Event_Type

import random

app = Flask(__name__)


app.secret_key = "SECRET_KEY"

app.jinja_env.undefined = StrictUndefined

DAYS_OF_THE_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday']


@app.route('/')
def index():
    """Homepage."""

    events = Event.query.all()

    locations = Location.query.all()

    event_types = Event_Type.query.all()

    return render_template('base.html', events=events, locations=locations, 
                           event_types=event_types, dow=DAYS_OF_THE_WEEK)


@app.route('/all_events')
def all_events():
    """Display a list of all events with information."""

    events = Event.query.all()

    return jsonify([event.serialize() for event in events])


@app.route('/all_locations')
def all_locations():
    """Display a list of all locations with information."""

    locations = Location.query.all()

    return jsonify([location.serialize() for location in locations])


@app.route('/all_event_types')
def all_event_types():
    """Display a list of all event types."""

    event_types = Event_Type.query.all()

    return jsonify([event_type.serialize() for event_type in event_types])


@app.route('/search_results')
def search_results():
    """Query database for given parameters."""

    base_query = Event.query

    if request.args.get('event_type'):
        chosen_types = request.args.getlist('event_type')

        base_query = base_query.filter(Event.type_id.in_(chosen_types))
        

    if request.args.get('weekday'):
        chosen_weekdays = request.args.getlist('weekday')

        base_query = base_query.filter(Event.weekday.in_(chosen_weekdays))

    if request.args.get('location'):
        chosen_location = request.args.get('location')

        chosen_string = f"%{chosen_location}%"

        base_query = base_query.join(Event.location).filter(Location.name.
            ilike(chosen_string))

    if request.args.get('city'):
        chosen_city = request.args.get('city')

        chosen_string = f"%{chosen_city}%"

        base_query = base_query.join(Event.location).filter(Location.city.
            ilike(chosen_string))

    if request.args.get('type_id'):
        chosen_type = request.args.get('type_id')

        base_query = base_query.filter(Event.type_id==chosen_type)

    event_results = base_query.all()

    return jsonify([event_result.serialize() for event_result in event_results])


@app.route('/featured_events')
def featured_events():
    """Display random events."""

    num_events = 0
    events_query = Event.query
    total_events = []

    for event in events_query:
        total_events.append(event.event_id)

    num_list = random.sample(total_events, 5)

    featured_events = events_query.filter(Event.event_id.in_(num_list))

    display_event = featured_events.all()

    return jsonify([feat_event.serialize() for feat_event in display_event])


@app.route('/more_event_info')
def more_event_info():
    """Display more information about a certain event."""

    event_id_res = request.args.get('event_id')
    event = Event.query.get(event_id_res)

    location_id_res = request.args.get('location_id')

    events_list = Event.query.filter(Event.location_id == location_id_res, Event.event_id != event_id_res).all()

    return jsonify(event.serialize(), [events.serialize() for events in events_list])


@app.route('/more_loc_info')
def more_loc_info():
    """Display more information about a certain location."""

    location_id_res = request.args.get('location_id')

    location = Location.query.get(location_id_res)

    events_list = Event.query.filter_by(location_id = location_id_res).all()

    return jsonify(location.serialize(), [events.serialize() for events in events_list])




if __name__ == "__main__":

    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
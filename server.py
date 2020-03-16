

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Event, Location, Event_Type



app = Flask(__name__)


app.secret_key = "SECRET_KEY"

app.jinja_env.undefined = StrictUndefined

DAYS_OF_THE_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday']


@app.route('/')
def index():
    """Homepage."""

    return render_template('homepage.html')


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

    # return render_template('all_locations.html', locations=locations)


@app.route('/all_event_types')
def all_event_types():
    """Display a list of all event types."""

    event_types = Event_Type.query.all()

    return render_template('all_event_types.html', event_types=event_types)


@app.route('/search_form_type')
def search_form_type():
    """Display search form for event type."""

    event_types = Event_Type.query.all()

    return render_template('search_form_type.html', event_types=event_types)


@app.route('/search_form_dow')
def search_form_dow():
    """Display seach form for day of the week."""

    return render_template('search_form_dow.html', dow=DAYS_OF_THE_WEEK)


@app.route('/search_type')
def search_type():
    """Display events given a certain type."""

    evt_type_id = request.args.get('typeofevent')

    events_type = Event.query.filter_by(type_id=evt_type_id).all()

    return render_template('events_type.html', events_type=events_type)


@app.route('/search_dow')
def search_dow():
    """Display event given a certain day of the week."""

    weekday = request.args.get('dayofweek')

    events_dow = Event.query.filter_by(weekday=weekday).all()

    return render_template('events_dow.html', events_dow=events_dow)


@app.route('/login')
def login_form():
    """Display form that collects users username and password."""

    return render_template('login_form.html')




if __name__ == "__main__":

    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
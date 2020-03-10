

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
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

    return render_template('all_events.html', events=events)


@app.route('/all_locations')
def all_locations():
    """Display a list of all locations with information."""

    locations = Location.query.all()

    return render_template('all_locations.html', locations=locations)


@app.route('/all_event_types')
def all_event_types():
    """Display a list of all event types."""

    event_types = Event_Type.query.all()

    return render_template('all_event_types.html', event_types=event_types)


@app.route('/search_forms')
def search_forms():
    """Display forms for different types of searches."""

    return render_template('search_forms.html', dow=DAYS_OF_THE_WEEK)


@app.route('/search_type')
def search_type():
    """Display events given a certain type."""

    return 'Hello'


@app.route('/search_dow')
def search_dow():
    """Display event given a certain day of the week."""

    weekday = request.args.get('weekday')

    events_dow = Event.query.filter_by(weekday=weekday).all()

    print(weekday)


if __name__ == "__main__":

    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
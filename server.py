

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Event, Location, Event_Type



app = Flask(__name__)


app.secret_key = "SECRET_KEY"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template('homepage.html')


@app.route('/search_type')
def search_type():
    """Display events given a certain type."""

    return 'Hello'


@app.route('/search_dow')
def search_dow():
    """Display event given a certain day of the week."""

    return 'Hey'


if __name__ == "__main__":

    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
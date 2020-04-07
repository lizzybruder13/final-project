

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Location(db.Model):
    """Location from database."""

    __tablename__ = "locations"


    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    zipcode = db.Column(db.Integer)

    def serialize(self):
        """ """
        return {
            'name':self.name, 'address':self.address, 
            'city':self.city, 'zipcode':self.zipcode, 'location_id':self.location_id
        }


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Location location_id={self.location_id} name={self.name}>"


class Event_Type(db.Model):
    """Types of events from database."""

    __tablename__ = "event_types"


    type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_name = db.Column(db.String)

    def serialize(self):
        """ """
        return {
            'name':self.type_name, 'type_id':self.type_id
        }

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Event_Type type_id={self.type_id} type_name={self.type_name}>"


class Event(db.Model):
    """Event from database."""

    __tablename__ = "events"


    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    type_id = db.Column(db.Integer, db.ForeignKey('event_types.type_id'))
    time = db.Column(db.Time)
    weekday = db.Column(db.String)

    location = db.relationship('Location', backref='event')
    event_type = db.relationship('Event_Type', backref='event')


    def serialize(self):
        """ """
        return {
            'event_id':self.event_id, 'location_id':self.location_id, 
            'location':self.location.name, 'zipcode':self.location.zipcode,
            'type':self.event_type.type_name, 'time':str(self.time),
            'weekday':self.weekday, 'city':self.location.city, 
            'address':self.location.address 
        }


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Event event_id={self.event_id} location_id={self.location_id} type_id={self.type_id}>"


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    is_authenticated = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)
    is_anonymous = db.Column(db.Boolean)

    def get_id(user_id):
        """Find user_id from table."""

        User.query.filter_by(user_id=user_id).one()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_ECHO'] = False 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bar_events'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":


    from server import app
    connect_to_db(app)
    print("Connected to DB.")
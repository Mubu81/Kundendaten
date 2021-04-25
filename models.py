#import os
from sqla_wrapper import SQLAlchemy
import os
import psycopg2

#db = os.environ['DATABASE_URL']

db = SQLAlchemy(os.getenv("DATABASE_URL")) # this connects to a database either on Heroku or on localhost
conn = psycopg2.connect(db, sslmode='require')

#db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))  # this connects to a database either on Heroku or on localhost

class Kundendaten(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String)
    nachname = db.Column(db.String)
    strasse = db.Column(db.String)
    hausnummer = db.Column(db.Integer)
    plz = db.Column(db.Integer)
    stadt = db.Column(db.String)
    email = db.Column(db.String)
    tel = db.Column(db.Integer)
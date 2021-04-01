import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "postgres://luejhxncqloyoe:e38f1cb714f6727eb4448563beaea4aa089e03b4ff4d3fd52b4cc6d4c590b53d@ec2-54-155-208-5.eu-west-1.compute.amazonaws.com:5432/den2l0igh4j0kh"))  # this connects to a database either on Heroku or on localhost


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
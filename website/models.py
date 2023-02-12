# from . import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    from_date = db.column(db.TIMESTAMP)
    to_date = db.column(db.TIMESTAMP)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.column(db.String(64))
    contact_mobile = db.column(db.String(64))


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.TIMESTAMP)
    employee_created = db.Column(db.Integer)
    client_id = db.Column(db.Integer)
    employee_id = db.Column(db.Integer)
    client_name = db.Column(db.String(64))
    client_contact = db.Column(db.String(64))
    start_time = db.Column(db.TIMESTAMP)
    end_time = db.Column(db.TIMESTAMP)
    price = db.Column(db.DECIMAL(10, 2))
    canceled = db.Column(db.BOOLEAN)


class ServiceBooked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointmend_id = db.Column(db.Integer)
    service_id = db.Column(db.Integer)
    price = db.Column(db.DECIMAL(10, 2))


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), unique=True, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)

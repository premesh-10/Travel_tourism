from flask import render_template
from app import app
from app.models import get_customers, get_bookings, get_cancellations, get_places

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers')
def customers():
    customers = get_customers()
    return render_template('customers.html', customers=customers)

@app.route('/bookings')
def bookings():
    bookings = get_bookings()
    return render_template('bookings.html', bookings=bookings)

@app.route('/cancellations')
def cancellations():
    cancellations = get_cancellations()
    return render_template('cancellations.html', cancellations=cancellations)

@app.route('/places')
def places():
    places = get_places()
    return render_template('places.html', places=places)
    
from app import mongo

def get_customers():
    return mongo.db.customers.find()

def get_bookings():
    return mongo.db.bookings.find()

def get_cancellations():
    return mongo.db.cancellations.find()

def get_places():
    return mongo.db.places.find()

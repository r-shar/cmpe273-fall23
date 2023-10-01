from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, VARCHAR, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/customerdb'
db = SQLAlchemy(app)

# create customer table 
class Customer(db.Model):
    customer_id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String, unique=True, nullable=False)
    last_name = db.Column(String, nullable=False)
    email = db.Column(VARCHAR, unique=True, nullable=False)
    created_on: Mapped[str] = db.Column(TIMESTAMP, nullable=False)

    def __init__(self, firstName, lastName, email, customerId=None, createdOn=None):
        self.customer_id = customerId
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.created_on = createdOn

    def __repr__(self):
        return f'<customer_id: {self.customer_id}, customer_name: {self.first_name} {self.last_name}, email: {self.email}, created_on: {self.created_on}>'

# get all customers
# format as List of Lists so it can be fed into Sheets API
@app.route('/customers')
def get_customers():
    
    res = [['customer_id', 'first_name', 'last_name', 'email']]
    
    customer_data = Customer.query.all()
    for customer in customer_data:
        res.append([
            customer.customer_id,
            customer.first_name,
            customer.last_name,
            customer.email
        ])

    return res

# insert customer record into db
@app.route('/customers/add')
def add_customer(firstName, lastName, email):

    new_customer = Customer(
            firstName=firstName,
            lastName=lastName,
            email=email,
            createdOn=datetime.now()
        )
    db.session.add(new_customer)
    db.session.commit()

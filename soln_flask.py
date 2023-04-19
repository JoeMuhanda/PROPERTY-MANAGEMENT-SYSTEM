import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///property.db'
db = SQLAlchemy(app)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    owner_name = db.Column(db.String(50), nullable=False)
    units = db.relationship('Unit', backref='property', lazy=True)

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    rent = db.Column(db.Float, nullable=False)
    deposit = db.Column(db.Float, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=True)

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    emergency_contact = db.Column(db.String(50), nullable=False)
    lease_start = db.Column(db.Date, nullable=False)
    lease_end = db.Column(db.Date, nullable=False)
    unit = db.relationship('Unit', backref='tenant', lazy=True)

@app.route('/')
def home():
    properties = Property.query.all()
    return render_template('home.html', properties=properties)

@app.route('/add_property', methods=['GET', 'POST'])
def add_property():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        owner_name = request.form['owner_name']
        property = Property(name=name, address=address, owner_name=owner_name)
        db.session.add(property)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_property.html')

@app.route('/view_property/<int:id>')
def view_property(id):
    property = Property.query.get_or_404(id)
    return render_template('view_property.html', property=property)

@app.route('/add_unit', methods=['GET', 'POST'])
def add_unit():
    if request.method == 'POST':
        number = request.form['number']
        size = request.form['size']
        rent = request.form['rent']
        deposit = request.form['deposit']
        property_id = request.form['property_id']
        unit = Unit(number=number, size=size, rent=rent, deposit=deposit, property_id=property_id)
        db.session.add(unit)
        db.session.commit()
        return redirect('/')
    else:
        properties = Property.query.all()
        return render_template('add_unit.html', properties=properties)

@app.route('/view_unit/<int:id>')
def view_unit(id):
    unit = Unit.query.get_or_404(id)
    return render_template('view_unit.html', unit=unit)

if __name__ == '__main__':
    app.run(debug=True)

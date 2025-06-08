from flask import Flask, render_template, request, redirect
from waitress import serve
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sohail2001@localhost/employee_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))
    address = db.Column(db.String(200))
    department = db.Column(db.String(50))
    working = db.Column(db.Boolean)

# Ensure tables are created
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/add', methods=['POST'])
def add_employee():
    emp = Employee(
        emp_id=request.form['emp_id'],
        name=request.form['name'],
        phone=request.form['phone'],
        address=request.form['address'],
        department=request.form['department'],
        working=True if request.form.get('working') == 'on' else False
    )
    try:
        db.session.add(emp)
        db.session.commit()
        return render_template('form.html', message="Employee added successfully!")
    except Exception as e:
        db.session.rollback()
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empcode = db.Column(db.Integer, unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Employee {self.firstname} {self.lastname}>'

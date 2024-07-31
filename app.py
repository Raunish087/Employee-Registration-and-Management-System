from flask import Flask, request, render_template, redirect, url_for
from config import Config
from models import db, Employee

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        empcode = request.form['empcode']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        password = request.form['password']
        status = request.form['status']

        new_employee = Employee(
            empcode=empcode,
            firstname=firstname,
            lastname=lastname,
            password=password,
            status=status
        )
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('index'))

    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

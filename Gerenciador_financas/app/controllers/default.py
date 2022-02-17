from flask import render_template, request
from app import app, db
from app.models.tables import Earnings, Spendings, Investiments


@app.route('/')
@app.route('/earnings')
def main():

    #new_earning = Earnings(2022, "February", 11, "Bosch Salary 1/2", 3000)
    #db.session.add(new_earning)
    #db.session.commit()
    earnings = Earnings.query.all()

    return render_template('earnings.html',earnings=earnings)


@app.route('/deletion/<int:id>')
def deletion(id=0):
    earning = Earnings.query.filter_by(id=id).first()
    return render_template('deletion.html', earning=earning)

@app.route('/save_deletion', methods=['POST'])
def save_deletion():
    id = int(request.form.get('id'))
    earning = Earnings.query.filter_by(id=id).first()
    db.session.delete(earning)
    db.session.commit()

    earnings = Earnings.query.all()

    return render_template('earnings.html', earnings=earnings)

@app.route('/edition/<int:id>')
def edition(id=0):
    earning = Earnings.query.filter_by(id=id).first()
    return render_template('edition.html', earning=earning)

@app.route('/save_edition', methods=['POST'])
def save_edition():
    Id = int(request.form.get('id'))
    Year = int(request.form.get('year'))
    Month = request.form.get('month')
    Day = int(request.form.get('day'))
    Description = request.form.get('description')
    Value = float(request.form.get('value'))
    print(f"{Year} {Month} {Day} {Description} {Value}")
    earning = Earnings.query.filter_by(id=Id).first()
    print(f"{earning.year} {earning.month} {earning.description}")
    earning.year = Year
    earning.month = Month
    earning.day = Day
    earning.description = Description
    earning.value = Value
    
    db.session.commit()

    earnings = Earnings.query.all()

    return render_template('earnings.html', earnings=earnings)

from app import db


class Earnings(db.Model):
    __tablename__ = 'earnings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer)
    month = db.Column(db.String(20))
    day = db.Column(db.Integer)
    description = db.Column(db.String(50))
    value = db.Column(db.Float)

    def __init__(self, year, month, day, description, value):
        self.year = year
        self.month = month.upper()
        self.day = day
        self.description = description.title()
        self.value = value
    
    def __repr__(self):
        return '<Earnings %r>' % self.description

class Spendings(db.Model):
    __tablename__ = 'spendings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer)
    month = db.Column(db.String(20))
    day = db.Column(db.Integer)
    description = db.Column(db.String(50))
    value = db.Column(db.Float)

    def __init__(self, year, month, day, description, value):
        self.year = year
        self.month = month.upper()
        self.day = day
        self.description = description.title()
        self.value = value
    
    def __repr__(self):
        return '<Spendings %r>' % self.description

class Investiments(db.Model):
    __tablename__ = 'investiments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer)
    month = db.Column(db.String(20))
    day = db.Column(db.Integer)
    description = db.Column(db.String(50))
    category = db.Column(db.String(20))
    coin = db.Column(db.String(5))
    value = db.Column(db.Float)

    def __init__(self, year, month, day, description, value, coin, category):
        self.year = year
        self.month = month.upper()
        self.day = day
        self.description = description.title()
        self.category = category.title()
        self.coin = coin.upper()
        self.value = value
    
    def __repr__(self):
        return '<Investiments %r>' % self.description

    
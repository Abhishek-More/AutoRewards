from bs4 import BeautifulSoup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(120))
    points = db.Column('points', db.String(120))

    def __repr__(self):
        return f"{self.email}".ljust(40) + str(self.points)

def scrapeInfo(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    scores = soup.find_all(id='id_rc')
    for score in scores:
        return score.text

def uploadData(email, points):

    user = User()
    user.email = email
    user.points = points
    found = User.query.filter_by(email=email).first()
    if found:
        User.query.filter_by(email=email).first().points = points
        users = User.query.filter_by().all()
        db.session.commit()
    else:
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as error:
            print(error)

def getUsers():
    users = User.query.all()
    return users
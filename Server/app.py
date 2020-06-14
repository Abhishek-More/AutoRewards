from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import automate as a
import info
import secrets
from selenium import webdriver

app = Flask(__name__)
app.config["SECRET_KEY"] = "1354233242532345"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column("id", db.Integer,primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    points = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.points}')"



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    method = "None"
    if request.method == "POST":
        method = "Post"
    if request.method == "GET":
        pass
    return method


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0')
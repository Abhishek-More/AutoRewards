from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import db_upload

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

@app.route("/")
def home():
    users = db_upload.getUsers()
    return render_template("index.html", content=users)

db.create_all()
#app.run(debug=True)
app.run(debug=False, host='0.0.0.0')
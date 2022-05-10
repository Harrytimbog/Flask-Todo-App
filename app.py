from flask import Flask, render_template, request
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

todos = ["Learn Flask", "Set up venv", "Build cool app"]

@app.route('/', methods=["GET", "POST"])
def index():
  return render_template("index.html", todos=todos)
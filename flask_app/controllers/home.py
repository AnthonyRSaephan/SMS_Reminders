import schedule, time
from flask_app import app
from flask import render_template
from flask_app.modules import helper


@app.route("/")
def homepage():
    return render_template("Homepage.html")

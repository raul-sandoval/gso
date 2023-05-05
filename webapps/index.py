########## Imports [START] ##########
from flask import render_template
from flask import flash
from webapps import app
########## Imports  [END]  ##########

########## @app.route("/") route [START] ##########
@app.route("/")
def index():
    flash(message='Loading data',category='info')
    return render_template('index.html')
########## @app.route("/") route  [END]  ##########

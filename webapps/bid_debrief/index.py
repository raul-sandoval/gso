########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.bid_debrief import APP_NAME
from webapps.bid_debrief import INPUT_PATH
from webapps.bid_debrief import LOG_PATH
from webapps.bid_debrief import OUTPUT_PATH
from webapps.bid_debrief import SQL_PATH
from webapps.bid_debrief import bid_debrief_blueprint
########## Imports [ END]  ##########

########## @bid_debrief_blueprint.route("/",methods=['GET']) [START] ##########
@bid_debrief_blueprint.route("/",methods=['GET'])
def index():
    response = {}

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/index.html')
########## @bid_debrief_blueprint.route("/",methods=['GET'])  [END]  ##########
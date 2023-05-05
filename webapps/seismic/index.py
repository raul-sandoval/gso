########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.seismic import APP_NAME
from webapps.seismic import INPUT_PATH
from webapps.seismic import LOG_PATH
from webapps.seismic import OUTPUT_PATH
from webapps.seismic import SQL_PATH
from webapps.seismic import seismic_blueprint
########## Imports [ END]  ##########

########## @seismic_blueprint.route("/",methods=['GET']) [START] ##########
@seismic_blueprint.route("/",methods=['GET'])
def index():
    response = {}

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/index.html')
########## @seismic_blueprint.route("/",methods=['GET'])  [END]  ##########
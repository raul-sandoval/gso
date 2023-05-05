########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.predictive_index import APP_NAME
from webapps.predictive_index import INPUT_PATH
from webapps.predictive_index import LOG_PATH
from webapps.predictive_index import OUTPUT_PATH
from webapps.predictive_index import SQL_PATH
from webapps.predictive_index import predictive_index_blueprint
########## Imports [ END]  ##########

########## @predictive_index_blueprint.route("/",methods=['GET']) [START] ##########
@predictive_index_blueprint.route("/",methods=['GET'])
def index():
    response = {}

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/index.html')
########## @predictive_index_blueprint.route("/",methods=['GET'])  [END]  ##########
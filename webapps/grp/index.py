########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.grp import APP_NAME
from webapps.grp import INPUT_PATH
from webapps.grp import LOG_PATH
from webapps.grp import OUTPUT_PATH
from webapps.grp import SQL_PATH
from webapps.grp import grp_blueprint
########## Imports [ END]  ##########

########## @grp_blueprint.route("/",methods=['GET']) [START] ##########
@grp_blueprint.route("/",methods=['GET'])
def index():
    response = {}

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/index.html')
########## @grp_blueprint.route("/",methods=['GET'])  [END]  ##########
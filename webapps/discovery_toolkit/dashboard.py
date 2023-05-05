########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.discovery_toolkit import APP_NAME
from webapps.discovery_toolkit import INPUT_PATH
from webapps.discovery_toolkit import LOG_PATH
from webapps.discovery_toolkit import OUTPUT_PATH
from webapps.discovery_toolkit import SQL_PATH
from webapps.discovery_toolkit import discovery_toolkit_blueprint
########## Imports [ END]  ##########

########## @discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST']) [START] ##########
@discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST'])
def dashboard():
    response = {}

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/dashboard.html',response=response)
########## @discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST'])  [END]  ##########
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

########## @discovery_toolkit_blueprint.route("/meetings",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("/meetings",methods=['GET'])
def meetings():
    response = {
        'type':'type',
        'account_id':'account_id',
    }
    return render_template(APP_NAME + '/meetings.html',response=response)
########## @discovery_toolkit_blueprint.route("/meetings",methods=['GET'])  [END]  ##########
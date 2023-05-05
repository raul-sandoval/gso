########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.monthly_commissions import APP_NAME
from webapps.monthly_commissions import INPUT_PATH
from webapps.monthly_commissions import LOG_PATH
from webapps.monthly_commissions import OUTPUT_PATH
from webapps.monthly_commissions import SQL_PATH
from webapps.monthly_commissions import monthly_commissions_blueprint
########## Imports [ END]  ##########

########## @monthly_commissions_blueprint.route("/",methods=['GET']) [START] ##########
@monthly_commissions_blueprint.route("/",methods=['GET'])
def index():
    response = {}

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/index.html')
########## @monthly_commissions_blueprint.route("/",methods=['GET'])  [END]  ##########
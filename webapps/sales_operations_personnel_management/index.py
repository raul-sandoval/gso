########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.sales_operations_personnel_management import APP_NAME
from webapps.sales_operations_personnel_management import INPUT_PATH
from webapps.sales_operations_personnel_management import LOG_PATH
from webapps.sales_operations_personnel_management import OUTPUT_PATH
from webapps.sales_operations_personnel_management import SQL_PATH
from webapps.sales_operations_personnel_management import sales_operations_personnel_management_blueprint
########## Imports [ END]  ##########

########## @sales_operations_personnel_management_blueprint.route("/",methods=['GET']) [START] ##########
@sales_operations_personnel_management_blueprint.route("/",methods=['GET'])
def index():
    response = {}

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/index.html')
########## @sales_operations_personnel_management_blueprint.route("/",methods=['GET'])  [END]  ##########
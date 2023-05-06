########## Imports [START] ##########
from faker import Faker
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
    fake = Faker()
    response = {
        'global_engagement': {
            'account_name': fake.company(),
            'account_id': fake.bothify(text='C#######'),
            'is_new_logo': ('Yes' if fake.boolean(chance_of_getting_true=25) else 'No'),
            'is_DNA': ('Yes' if fake.boolean(chance_of_getting_true=60) else 'No'),
            'is_GNA': ('Yes' if fake.boolean(chance_of_getting_true=50) else 'No'),
            'is_GTDP': ('Yes' if fake.boolean(chance_of_getting_true=25) else 'No'),
            'is_ADP': ('Yes' if fake.boolean(chance_of_getting_true=10) else 'No'),
            'is_Account_Management': ('Yes' if fake.boolean(chance_of_getting_true=50) else 'No'),
        },
    }

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/dashboard.html',response=response)
########## @discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST'])  [END]  ##########
########## Imports [START] ##########
from flask import Flask
from flask_session import Session
from webapps.bid_debrief import bid_debrief_blueprint
from webapps.discovery_toolkit import discovery_toolkit_blueprint
from webapps.grp import grp_blueprint
from webapps.monthly_commissions import monthly_commissions_blueprint
from webapps.predictive_index import predictive_index_blueprint
from webapps.seismic import seismic_blueprint
from webapps.sales_operations_personnel_management import sales_operations_personnel_management_blueprint
########## Imports  [END]  ##########

########## Setup app [START] ##########
app = Flask(__name__)
app.config.from_object('config')
Session(app)
########## Setup app  [END]  ##########

########## Import routes [START] ##########
import webapps.index
########## Import routes  [END]  ##########

########## Register apps [START] ##########
app.register_blueprint(bid_debrief_blueprint, url_prefix='/bid_debrief')
app.register_blueprint(discovery_toolkit_blueprint, url_prefix='/discovery_toolkit')
app.register_blueprint(grp_blueprint, url_prefix='/grp')
app.register_blueprint(monthly_commissions_blueprint, url_prefix='/monthly_commissions')
app.register_blueprint(predictive_index_blueprint, url_prefix='/predictive_index')
app.register_blueprint(seismic_blueprint, url_prefix='/seismic')
app.register_blueprint(sales_operations_personnel_management_blueprint, url_prefix='/sales_operations_personnel_management')
########## Register apps  [END]  ##########
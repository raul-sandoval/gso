########## Imports [START] ##########
from flask import Flask
from flask_session import Session
from webapps.discovery_toolkit import discovery_toolkit_blueprint
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
app.register_blueprint(discovery_toolkit_blueprint, url_prefix='/discovery_toolkit')
########## Register apps  [END]  ##########
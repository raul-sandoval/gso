########## Imports [START] ##########
from flask import Flask
from flask_session import Session
########## Imports  [END]  ##########

########## Setup app [START] ##########
app = Flask(__name__)
app.config.from_object('config')
Session(app)
########## Setup app  [END]  ##########

########## Import routes [START] ##########
import webapps.index
########## Import routes  [END]  ##########

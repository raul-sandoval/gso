########## Imports [START] ##########
from config import INPUT_PATH
from config import LOG_PATH
from config import OUTPUT_PATH
from config import SQL_PATH
from flask import Blueprint
########## Imports  [END]  ##########

########## Global variables [START] ##########
APP_NAME = 'seismic'
INPUT_PATH = INPUT_PATH + APP_NAME + '\\'
LOG_PATH = LOG_PATH + APP_NAME + '\\'
OUTPUT_PATH = OUTPUT_PATH + APP_NAME + '\\'
SQL_PATH = SQL_PATH + APP_NAME + '\\'
seismic_blueprint = Blueprint(APP_NAME,__name__,static_folder='static',template_folder='templates')
########## Global variables  [END]  ##########

########## Import routes [START] ##########
import webapps.seismic.index
########## Import routes  [END]  ##########
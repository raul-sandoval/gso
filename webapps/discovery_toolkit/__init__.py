########## Imports [START] ##########
from config import INPUT_PATH
from config import LOG_PATH
from config import OUTPUT_PATH
from config import SQL_PATH
from flask import Blueprint
########## Imports  [END]  ##########

########## Global variables [START] ##########
APP_NAME = 'discovery_toolkit'
INPUT_PATH = INPUT_PATH + APP_NAME + '\\'
LOG_PATH = LOG_PATH + APP_NAME + '\\'
OUTPUT_PATH = OUTPUT_PATH + APP_NAME + '\\'
SQL_PATH = SQL_PATH + APP_NAME + '\\'
discovery_toolkit_blueprint = Blueprint(APP_NAME,__name__,static_folder='static',template_folder='templates')
########## Global variables  [END]  ##########

########## Import routes [START] ##########
import webapps.discovery_toolkit.dashboard
import webapps.discovery_toolkit.download_duns_location_report
import webapps.discovery_toolkit.download_global_engagement_report
import webapps.discovery_toolkit.download_meetings_information_report
import webapps.discovery_toolkit.download_opportunities_information_report
import webapps.discovery_toolkit.index
import webapps.discovery_toolkit.meetings
########## Import routes  [END]  ##########
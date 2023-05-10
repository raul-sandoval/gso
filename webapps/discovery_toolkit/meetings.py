########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.database import vizcrm_get
from webapps.discovery_toolkit import APP_NAME
from webapps.discovery_toolkit import INPUT_PATH
from webapps.discovery_toolkit import LOG_PATH
from webapps.discovery_toolkit import OUTPUT_PATH
from webapps.discovery_toolkit import SQL_PATH
from webapps.discovery_toolkit import discovery_toolkit_blueprint
from webapps.discovery_toolkit.functions import fnGetAccountName
import json
import pandas as pd
########## Imports [ END]  ##########

########## @discovery_toolkit_blueprint.route("/meetings/<account_id>/<type_id>",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("/meetings/<account_id>/<type_id>",methods=['GET'])
def meetings(account_id,type_id):

    MEETING_METHOD_CODE = "('PHONE','WEB')" if type_id == 'PHONE' or type_id == 'WEB' else "('" + type_id + "')"
    fd = open(SQL_PATH + 'get_meetings_details.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",account_id)
    strQuery = strQuery.replace("${MEETING_METHOD_CODE}",MEETING_METHOD_CODE) if MEETING_METHOD_CODE != "('all')" else strQuery.replace("AND (M.MEETING_METHOD_CODE IN ${MEETING_METHOD_CODE})",'')

    df_input = vizcrm_get(strQuery)

    df_input['meeting_start_date_time'] = pd.to_datetime(df_input.meeting_start_date_time)
    df_input['meeting_start_date_time'] = df_input['meeting_start_date_time'].dt.strftime('%m/%d/%Y %X')
    df_input['email_address'] = df_input['email_address'].str.lower()

    records = df_input.to_json(orient="table")
    parsed = json.loads(records)
    json.dumps(parsed, indent=4)
    records = parsed

    match type_id:
        case 'INPERSON':
            meeting_type = 'In person meetings'
        case 'WEB':
            meeting_type = 'Phone/Web meetings'
        case 'PHONE':
            meeting_type = 'Phone/Web meetings'
        case _:
            meeting_type = 'Others meetings'

    response = {
        'records' : records,
        'account_id' : account_id,
        'type_id' : type_id,
        'meeting_type' : meeting_type,
        'account_name' : fnGetAccountName(account_id),
    }
    return render_template(APP_NAME + '/meetings.html',response=response)
########## @discovery_toolkit_blueprint.route("/meetings/<account_id>/<type_id>",methods=['GET'])  [END]  ##########
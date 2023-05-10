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

########## @discovery_toolkit_blueprint.route("/opportunities/<account_id>/<type_id>",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("/opportunities/<account_id>/<type_id>",methods=['GET'])
def opportunities(account_id,type_id):

    fd = open(SQL_PATH + 'get_opportunities_details.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",account_id)
    strQuery = strQuery.replace("${OPPORTUNITY_STATUS_CODE}",type_id)

    df_input = vizcrm_get(strQuery)

    df_input['last_modification_date_time'] = pd.to_datetime(df_input.last_modification_date_time)
    df_input['last_modification_date_time'] = df_input['last_modification_date_time'].dt.strftime('%m/%d/%Y')
    df_input['email_address'] = df_input['email_address'].str.lower()

    records = df_input.to_json(orient="table")
    parsed = json.loads(records)
    json.dumps(parsed, indent=4)
    records = parsed

    match type_id:
        case 'WON':
            opportunity_type = 'Won opportunities'
        case 'ACTIVE':
            opportunity_type = 'Active opportunities'
        case 'HOLD':
            opportunity_type = 'On Hold opportunities'
        case 'LOST':
            opportunity_type = 'Lost opportunities'
        case _:
            opportunity_type = 'Others opportunities'

    response = {
        'records' : records,
        'account_id' : account_id,
        'type_id' : type_id,
        'opportunity_type' : opportunity_type,
        'account_name' : fnGetAccountName(account_id),
    }
    return render_template(APP_NAME + '/opportunities.html',response=response)
########## @discovery_toolkit_blueprint.route("/opportunities/<account_id>/<type_id>",methods=['GET'])  [END]  ##########
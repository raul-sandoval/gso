########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.discovery_toolkit import APP_NAME
from webapps.discovery_toolkit import INPUT_PATH
from webapps.discovery_toolkit import LOG_PATH
from webapps.discovery_toolkit import OUTPUT_PATH
from webapps.discovery_toolkit import SQL_PATH
from webapps.discovery_toolkit import discovery_toolkit_blueprint
from webapps.discovery_toolkit.functions import fnGetAccountName
from webapps.discovery_toolkit.functions import fnGetGSE_GTDP_DNA
import json
import pandas as pd
########## Imports [END] ##########

########## @discovery_toolkit_blueprint.route("/gtdp/<account_id>",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("/gtdp/<account_id>",methods=['GET'])
def gtdp(account_id):
    df_data =  pd.DataFrame()
    df_no_revenue = pd.DataFrame()
    df_existing = pd.DataFrame()
    df_new_business = pd.DataFrame()

    df_data = fnGetGSE_GTDP_DNA(account_id,'GTDP',False)
    
    df_no_revenue = df_data[df_data['STATUS']=='NO REVENUE']
    df_existing = df_data[df_data['STATUS']=='Existing']
    df_new_business = df_data[df_data['STATUS']=='New Business']

    no_revenue_list = (1 if len(df_no_revenue) > 0 else 0)
    existing_list = (1 if len(df_existing) > 0 else 0)
    new_business_list = (1 if len(df_new_business) > 0 else 0)

    new_business = df_new_business.to_json(orient="table")
    parsed = json.loads(new_business)
    json.dumps(parsed, indent=4)
    new_business = parsed

    no_revenue = df_no_revenue.to_json(orient="table")
    parsed = json.loads(no_revenue)
    json.dumps(parsed, indent=4)
    no_revenue = parsed

    existing = df_existing.to_json(orient="table")
    parsed = json.loads(existing)
    json.dumps(parsed, indent=4)
    existing = parsed

    response = {
        'account_id' : account_id,
        'account_name' : fnGetAccountName(account_id),
        'no_revenue':no_revenue,
        'existing':existing,
        'new_business':new_business,
        'column_size':int(12/(1 if no_revenue_list+existing_list+new_business_list == 0 else no_revenue_list+existing_list+new_business_list))
    }
    return render_template(APP_NAME + '/gtdp.html',response=response)
########## @discovery_toolkit_blueprint.route("/gtdp/<account_id>",methods=['GET'])  [END]  ##########
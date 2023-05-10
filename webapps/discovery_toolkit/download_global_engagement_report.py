########## Imports [START] ##########
from flask import flash
from flask import make_response
from webapps.database import vizcrm_get
from webapps.discovery_toolkit import SQL_PATH
from webapps.discovery_toolkit import discovery_toolkit_blueprint
import io
import pandas as pd
########## Imports [END] ##########

########## @discovery_toolkit_blueprint.route("dashboard/download_global_engagement_report/<account_id>",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("dashboard/download_global_engagement_report/<account_id>",methods=['GET'])
def download_global_engagement_report(account_id):

    df_input = pd.DataFrame()
    fd = open(SQL_PATH + 'get_global_engagement.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",account_id)
    df_input = vizcrm_get(strQuery)

    # Creating output and writer (pandas excel writer)
    out = io.BytesIO()
    writer = pd.ExcelWriter(out, engine='xlsxwriter')   
    # Export data frame to excel
    df_input.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
    writer.close()
    # Flask create response 
    r = make_response(out.getvalue())    
    # Defining correct excel headers
    r.headers["Content-Disposition"] = "attachment; filename=global_engagement.xlsx"
    r.headers["Content-type"] = "application/x-xls"
    # Finally return response
    return r
########## @discovery_toolkit_blueprint.route("dashboard/download_global_engagement_report/<account_id>",methods=['GET'])  [END]  ##########

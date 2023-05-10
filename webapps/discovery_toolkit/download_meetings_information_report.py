########## Imports [START] ##########
from flask import flash
from flask import make_response
from flask import redirect
from flask import session
from flask import url_for
from webapps.database import vizcrm_get
from webapps.discovery_toolkit import SQL_PATH
from webapps.discovery_toolkit import discovery_toolkit_blueprint
import io
import pandas as pd
########## Imports [END] ##########

########## @discovery_toolkit_blueprint.route("dashboard/download_meetings_information_report/<account_id>",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("dashboard/download_meetings_information_report/<account_id>",methods=['GET'])
def download_meetings_information_report(account_id):
    fd = open(SQL_PATH + 'get_meetings_details.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",account_id)
    strQuery = strQuery.replace("AND (M.MEETING_METHOD_CODE IN ${MEETING_METHOD_CODE})",'')
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
    r.headers["Content-Disposition"] = "attachment; filename=meetings_details.xlsx"
    r.headers["Content-type"] = "application/x-xls"
    # Finally return response
    return r
########## @discovery_toolkit_blueprint.route("dashboard/download_meetings_information_report/<account_id>",methods=['GET'])  [END]  ##########
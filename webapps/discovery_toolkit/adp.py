########## Imports [START] ##########
from flask import flash
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from webapps.discovery_toolkit.functions import fnGetAccountName
from webapps.discovery_toolkit.functions import fnGetGSE_GTDP_DNA
from webapps.discovery_toolkit.index import APP_NAME
from webapps.discovery_toolkit.index import discovery_toolkit_blueprint
import json
import pandas as pd
########## Imports  [END]  ##########

########## @discovery_toolkit_blueprint.route("/adp/<account_id>",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("/adp/<account_id>",methods=['GET'])
def adp(account_id):

    df_dna_adp = pd.DataFrame()
    df_gtdp_adp = pd.DataFrame()

    df_dna_adp = fnGetGSE_GTDP_DNA(account_id,'DNA',False)
    df_dna_adp = df_dna_adp.loc[(df_dna_adp['ADP']=='YES')]
    dna_adp = df_dna_adp.to_json(orient="table")
    parsed = json.loads(dna_adp)
    json.dumps(parsed, indent=4)
    dna_adp = parsed

    df_gtdp_adp = fnGetGSE_GTDP_DNA(account_id,'GTDP',False)
    df_gtdp_adp = df_gtdp_adp.loc[(df_gtdp_adp['ADP']=='YES')]
    gtdp_adp = df_gtdp_adp.to_json(orient="table")
    parsed = json.loads(gtdp_adp)
    json.dumps(parsed, indent=4)
    gtdp_adp = parsed

    response = {
        'account_id' : account_id,
        'account_name' : fnGetAccountName(account_id),
        'dna_adp':dna_adp,
        'gtdp_adp':gtdp_adp,
    }
    return render_template(APP_NAME + '/adp.html',response=response)
########## @discovery_toolkit_blueprint.route("/adp/<account_id>",methods=['GET'])  [END]  ##########
########## Imports [START] ##########
from flask import flash
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from webapps.discovery_toolkit.functions import fnGetGSE_GTDP_DNA
from webapps.discovery_toolkit.index import APP_NAME
from webapps.discovery_toolkit.index import discovery_toolkit_blueprint
import json
import pandas as pd
########## Imports  [END]  ##########

########## @discovery_toolkit_blueprint.route("/adp",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("/adp",methods=['GET'])
def adp():
    if not session.get("email"):
        return redirect(url_for('login',next='discovery_toolkit.dna'))
    
    if not session.get("toolkit_account_id"):
        return redirect(url_for('discovery_toolkit.root'))
    account_id = session['toolkit_account_id']
    
    flash(message='Loading data',category='info')
    df_dna_adp = pd.DataFrame()
    df_gtdp_adp = pd.DataFrame()

    df_dna_adp = fnGetGSE_GTDP_DNA(account_id,'DNA',False)
    df_dna_adp = df_dna_adp.loc[(df_dna_adp['ADP']=='YES')]
    dna_adp = df_dna_adp.to_json(orient="table")
    parsed = json.loads(dna_adp)
    json.dumps(parsed, indent=4)
    dna_adp = parsed

    df_gtdp_adp = fnGetGSE_GTDP_DNA(account_id,'DNA',False)
    df_gtdp_adp = df_gtdp_adp.loc[(df_gtdp_adp['ADP']=='YES')]
    gtdp_adp = df_gtdp_adp.to_json(orient="table")
    parsed = json.loads(gtdp_adp)
    json.dumps(parsed, indent=4)
    gtdp_adp = parsed

    gtdp_adp = fnGetGSE_GTDP_DNA(account_id,'GTDP',False)

    response = {
        'dna_adp':dna_adp,
        'gtdp_adp':gtdp_adp,
    }
    return render_template(APP_NAME + 'adp.html',response=response)
########## @discovery_toolkit_blueprint.route("/adp",methods=['GET'])  [END]  ##########
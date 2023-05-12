########## Imports [START] ##########
from flask import flash
from flask import render_template
from webapps.discovery_toolkit import APP_NAME
from webapps.discovery_toolkit import INPUT_PATH
from webapps.discovery_toolkit import LOG_PATH
from webapps.discovery_toolkit import OUTPUT_PATH
from webapps.discovery_toolkit import SQL_PATH
from webapps.discovery_toolkit import discovery_toolkit_blueprint
from webapps.discovery_toolkit.functions import fnGetAccountManagementLevel
from webapps.discovery_toolkit.functions import fnGetAccountName
import json
import math
import pandas as pd
########## Imports [ END]  ##########

########## @discovery_toolkit_blueprint.route("/account_management/<account_id>",methods=['GET']) [START] ##########
@discovery_toolkit_blueprint.route("/account_management/<account_id>",methods=['GET'])
def account_management(account_id):

    df_cam = pd.DataFrame()
    df_dist = pd.DataFrame()
    df_gam = pd.DataFrame()
    df_lam = pd.DataFrame()
    df_sales_pileline = pd.DataFrame()
    cam_owner = '-'
    cam_list = 0
    dist_owner = '-'
    dist_list = 0
    gam_owner = '-'
    gam_list = 0
    lam_owner = '-'
    lam_list = 0
    sales_pileline_owner = '-'
    sales_pileline_list = 0

    df_cam,df_dist,df_gam,df_lam,df_sales_pileline = fnGetAccountManagementLevel(account_id,True)
    

    if len(df_cam) > 0:
        cam_owner = df_cam['owner_name'][0] + ", " + df_cam['owner_title'][0] + ", " + df_cam['owner_branch'][0]
        cam_list = 1

    if len(df_dist) > 0:
        dist_owner = df_dist['owner_name'][0] + ", " + df_dist['owner_title'][0] + ", " + df_dist['owner_branch'][0]
        dist_list = 1

    if len(df_gam) > 0:
        gam_owner = df_gam['owner_name'][0] + ", " + df_gam['owner_title'][0] + ", " + df_gam['owner_branch'][0]
        gam_list = 1

    if len(df_lam) > 0:
        lam_owner = df_lam['owner_name'][0] + ", " + df_lam['owner_title'][0] + ", " + df_lam['owner_branch'][0]
        lam_list = 1
    
    if len(df_sales_pileline) > 0:
        sales_pileline_owner = df_sales_pileline['owner_name'][0] + ", " + df_sales_pileline['owner_title'][0] + ", " + df_sales_pileline['owner_branch'][0]
        sales_pileline_list = 1
    


    column_size = int(12/(1 if cam_list+dist_list+gam_list+lam_list+sales_pileline_list == 0 else cam_list+dist_list+gam_list+lam_list+sales_pileline_list))
    column_size = math.floor(column_size)
    cam = df_cam.to_json(orient="table")
    parsed = json.loads(cam)
    json.dumps(parsed, indent=4)
    cam = parsed

    dist = df_dist.to_json(orient="table")
    parsed = json.loads(dist)
    json.dumps(parsed, indent=4)
    dist = parsed

    gam = df_gam.to_json(orient="table")
    parsed = json.loads(gam)
    json.dumps(parsed, indent=4)
    gam = parsed

    lam = df_lam.to_json(orient="table")
    parsed = json.loads(lam)
    json.dumps(parsed, indent=4)
    lam = parsed

    sales_pileline = df_sales_pileline.to_json(orient="table")
    parsed = json.loads(sales_pileline)
    json.dumps(parsed, indent=4)
    sales_pileline = parsed

    response = {
        'account_id' : account_id,
        'account_name' : fnGetAccountName(account_id),
        'cam_owner':cam_owner,
        'dist_owner':dist_owner,
        'gam_owner':gam_owner,
        'lam_owner':lam_owner,
        'sales_pileline_owner':sales_pileline_owner,
        'cam': cam,
        'dist': dist,
        'gam': gam,
        'lam': lam,
        'sales_pileline': sales_pileline,
        'column_size':column_size
    }
    return render_template(APP_NAME + '/account_management.html',response=response)
########## @discovery_toolkit_blueprint.route("/account_management/<account_id>",methods=['GET'])  [END]  ##########
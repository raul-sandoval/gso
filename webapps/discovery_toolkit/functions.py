########## Imports [START] ##########
from webapps.database import gso_get
from webapps.database import vizcrm_get
from webapps.discovery_toolkit import SQL_PATH
import pandas as pd
########## Imports  [END]  ##########

########## def fnGetAccountName(pAccountId): [START] ##########
def fnGetAccountName(pAccountId):
    df_input =  pd.DataFrame()
    fd = open(SQL_PATH + 'get_account_name.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",pAccountId)
    df_input = vizcrm_get(strQuery)
    name = (df_input['name'][0] if df_input.size != 0 else "-")
    return name
########## def fnGetAccountName(pAccountId):  [END]  ##########

########## def fnGetGSE_GTDP_DNA(pAccountId,pProgram,pAllRecords=False): [START] ##########
def fnGetGSE_GTDP_DNA(pAccountId,pProgram,pAllRecords=False):

    fd = open(SQL_PATH + 'get_gse_gtdp_dna.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",pAccountId)
    strQuery = strQuery.replace("${Program}",pProgram)
    df_input = gso_get(strQuery)
    if pAllRecords:
        total_records = len(df_input[df_input['STATUS']!='NO REVENUE'])
        total_adp = len(df_input[(df_input['ADP']=='YES') & (df_input['STATUS']!='NO REVENUE')])
        return total_records,total_adp
    else:
        return df_input
########## def fnGetGSE_GTDP_DNA(pAccountId,pProgram,pAllRecords=False):  [END]  ##########

########## def fnGetAccountManagement(pAccountId): [START] ##########
def fnGetAccountManagement(pAccountId,pDataFrames=False):
    fd = open(SQL_PATH + 'get_account_programs.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",pAccountId)
    df_input = vizcrm_get(strQuery)
    df_input = df_input.drop_duplicates(subset='gci_number', keep="first")
    
    cam = df_input[df_input['acc_management'].str.contains("CAM")]
    dist = df_input[df_input['acc_management'].str.contains("DIST")]
    gam = df_input[df_input['acc_management'].str.contains("GAM")]
    lam = df_input[df_input['acc_management'].str.contains("LAM")]
    sales_pileline = df_input[df_input['acc_management'].str.contains("Sales Pipeline")]
    if not pDataFrames:
        cam = len(df_input[df_input['acc_management'].str.contains("CAM")])
        dist = len(df_input[df_input['acc_management'].str.contains("DIST")])
        gam = len(df_input[df_input['acc_management'].str.contains("GAM")])
        lam = len(df_input[df_input['acc_management'].str.contains("LAM")])
        sales_pileline = len(df_input[df_input['acc_management'].str.contains("Sales Pipeline")])
    
    return cam,dist,gam,lam,sales_pileline
########## def fnGetAccountManagement(pAccountId): [END] ##########

########## def fnGetDunsByAccountId(pAccountId): [START] ##########
def fnGetDunsByAccountId(pAccountId):
    df_input = pd.DataFrame()
    fd = open(SQL_PATH + 'get_duns_by_account_id.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",pAccountId)
    df_input = vizcrm_get(strQuery)

    df_tmp1 = df_input.groupby('country_name')['has_gci_match'].apply(lambda x: (x=='YES').sum()).reset_index(name='YES')
    df_tmp2 = df_input.groupby('country_name')['has_gci_match'].apply(lambda x: (x=='NO').sum()).reset_index(name='NO')
    df_tmp = pd.merge(df_tmp1, df_tmp2, on='country_name')
    df_tmp = df_tmp.sort_values(by=['NO','YES'],ascending=False)
    df_tmp = df_tmp[0:10]

    total_locations = len(df_input)

    countries =  df_tmp['country_name'].values.tolist()
    gci_match_yes = df_tmp['YES'].values.tolist()
    gci_match_no = df_tmp['NO'].values.tolist()

    df_input = pd.DataFrame()
    fd = open(SQL_PATH + 'get_total_gci_matches.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",pAccountId)
    df_input = vizcrm_get(strQuery)

    total_gci_matches = df_input['Total_GCI_Matches'][0]
    return total_locations,total_gci_matches,countries,gci_match_yes,gci_match_no
########## def fnGetDunsByAccountId(pAccountId):  [END]  ##########

########## def fnGetCountOfMeetings(pAccountId): [START] ##########
def fnGetCountOfMeetings(pAccountId):
    df_tmp = pd.DataFrame()

    fd = open(SQL_PATH + 'get_count_of_meetings.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",pAccountId)
    df_input = vizcrm_get(strQuery)

    df_tmp = df_input.groupby(['owning_branch_code'])['meeting_key'].count().reset_index(name='Total').sort_values(by=['Total'],ascending=False)
    df_tmp = df_tmp[0:20]

    branches = df_tmp["owning_branch_code"].values.tolist()
    completed_meetings = df_tmp["Total"].values.tolist()
    total_phone_web = len(df_input[df_input['method_code']=='PHONE']) + len(df_input[df_input['method_code']=='WEB'])
    total_in_person = len(df_input[df_input['method_code']=='INPERSON'])

    response = (branches,completed_meetings,total_phone_web,total_in_person)

    return response
########## def fnGetCountOfMeetings(pAccountId):  [END]  ##########

########## def fnGetCountOfOpportunities(pAccountId): [START] ##########
def fnGetCountOfOpportunities(pAccountId):
    chart = pd.DataFrame()

    fd = open(SQL_PATH + 'get_count_of_opportunities.sql')
    strQuery = fd.read()
    fd.close()
    strQuery = strQuery.replace("${Account_Id}",pAccountId)
    df_input = vizcrm_get(strQuery)

    active_opps = df_input[df_input['opportunity_status_code']=='ACTIVE']
    active_opps = active_opps.groupby(["owning_branch_code"])[
        "opportunity_key"].count().reset_index()

    won_opps = df_input[df_input['opportunity_status_code']=='WON']
    won_opps = won_opps.groupby(["owning_branch_code"])[
        "opportunity_key"].count().reset_index()

    chart = pd.merge(won_opps,active_opps,how='outer',on='owning_branch_code')

    active = len(df_input[df_input['opportunity_status_code']=='ACTIVE'])
    lost = len(df_input[df_input['opportunity_status_code']=='LOST'])
    on_hold = len(df_input[df_input['opportunity_status_code']=='ON_HOLD'])
    won = len(df_input[df_input['opportunity_status_code']=='WON'])
    opp_branches = chart["owning_branch_code"].values.tolist()
    opp_active = chart['opportunity_key_x'].values.tolist()
    opp_won = chart['opportunity_key_y'].values.tolist()

    response = (active,lost,on_hold,won,opp_branches,opp_active,opp_won)

    return response
########## def fnGetCountOfOpportunities(pAccountId):  [END]  ##########
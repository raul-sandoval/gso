########## Imports [START] ##########
from faker import Faker
from flask import flash
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from webapps.discovery_toolkit import APP_NAME
from webapps.discovery_toolkit import INPUT_PATH
from webapps.discovery_toolkit import LOG_PATH
from webapps.discovery_toolkit import OUTPUT_PATH
from webapps.discovery_toolkit import SQL_PATH
from webapps.discovery_toolkit import discovery_toolkit_blueprint
from webapps.discovery_toolkit.functions import fnGetAccountManagement
from webapps.discovery_toolkit.functions import fnGetAccountName
from webapps.discovery_toolkit.functions import fnGetCountOfMeetings
from webapps.discovery_toolkit.functions import fnGetCountOfOpportunities
from webapps.discovery_toolkit.functions import fnGetDunsByAccountId
from webapps.discovery_toolkit.functions import fnGetGSE_GTDP_DNA
########## Imports [ END]  ##########

########## @discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST']) [START] ##########
@discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST'])
def dashboard():

    if request.method == 'GET':
        account_id = (session.get('toolkit_account_id') if ('toolkit_account_id' in session) else '-')
    else:
        account_id = (request.form.get('account_id') if ('account_id' in request.form) else '-')

    account_id = account_id.upper()
    session['toolkit_account_id'] = account_id


    account_name = fnGetAccountName(account_id)

    is_DNA = '-'
    is_DNA,dna_adp = fnGetGSE_GTDP_DNA(account_id,'DNA',True)
    is_DNA = ('Yes' if is_DNA > 0 else 'No')

    is_GNA = '-'
    is_GNA,gna_adp = fnGetGSE_GTDP_DNA(account_id,'GSE',True)
    is_GNA = ('Yes' if is_GNA > 0 else 'No')

    is_GTDP =  '-'
    is_GTDP,gtdp_adp = fnGetGSE_GTDP_DNA(account_id,'GTDP',True)
    is_GTDP = ('Yes' if is_GTDP > 0 else 'No')

    is_ADP = '-'
    is_ADP = ('Yes' if (dna_adp + gna_adp + gtdp_adp) > 0 else 'No')

    is_cam,is_dist,is_gam,is_lam,is_sales_pileline = fnGetAccountManagement(account_id)
    is_Account_Management = '-'
    is_Account_Management = ('Yes' if is_cam > 0 or is_dist > 0 or is_gam > 0 or is_lam > 0 or is_sales_pileline > 0 else 'No')

    total_locations,total_gci_matches,duns_countries,duns_gci_matches,duns_gci_no_matches = fnGetDunsByAccountId(account_id)

    (meeting_branches,total_meetings,total_phone_web_meetings,total_in_person_meetings) = fnGetCountOfMeetings(account_id)
    (total_active_opportunities,total_lost_opportunities,total_on_hold_opportunities,total_won_opportunities,active_won_opps_branches,active_opportunities,won_opportunities) = fnGetCountOfOpportunities(account_id)

    fake = Faker()

    response = {
        'global_engagement': {
            'account_name' : account_name,
            'account_id' : account_id,
            'is_new_logo' : ('Yes' if fake.boolean(chance_of_getting_true=25) else 'No'),
            'DNA' : {
                'is_DNA': is_DNA,
                'url': ('dna/' + account_id if is_DNA == 'Yes' else '#'),
            },
            'GNA' : {
                'is_GNA': is_GNA,
                'url': ('gna/' + account_id if is_GNA == 'Yes' else '#'),
            },
            'GTDP' : {
                'is_GTDP': is_GTDP,
                'url': ('gtdp/' + account_id if is_GTDP == 'Yes' else '#'),
            },
            'ADP' : {
                'is_ADP': is_ADP,
                'url': ('adp/' + account_id if is_ADP == 'Yes' else '#'),
            },
            'Account_Management' : {
                'is_Account_Management': is_Account_Management,
                'url': ('account_management/' + account_id if is_Account_Management == 'Yes' else '#'),
            },
        },
        'duns_locations': {
            'total_gci_matches' : total_gci_matches,
            'total_locations' : total_locations,
            'duns_locations_chart' : {
                'duns_countries': duns_countries,
                'duns_gci_matches': duns_gci_matches,
                'duns_gci_no_matches': duns_gci_no_matches,
            },
        },
        'meetings_information' : {
            'total_in_person_meetings': total_in_person_meetings,
            'total_phone_web_meetings': total_phone_web_meetings,
            'total_won_opportunities': total_won_opportunities,
            'total_active_opportunities': total_active_opportunities,
            'total_on_hold_opportunities': total_on_hold_opportunities,
            'total_lost_opportunities': total_lost_opportunities,
            'meetings_activity_chart' : {
                'branches' : meeting_branches,
                'total_meetings' : total_meetings,
            },
            'active_won_opps_chart' : {
                'branches' : active_won_opps_branches,
                'won_opportunities' : won_opportunities,
                'active_opportunities' : active_opportunities,
            },
        },
    }

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/dashboard.html',response=response)
########## @discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST'])  [END]  ##########
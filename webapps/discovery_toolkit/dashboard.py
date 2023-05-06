########## Imports [START] ##########
from faker import Faker
from flask import flash
from flask import render_template
from webapps.discovery_toolkit import APP_NAME
from webapps.discovery_toolkit import INPUT_PATH
from webapps.discovery_toolkit import LOG_PATH
from webapps.discovery_toolkit import OUTPUT_PATH
from webapps.discovery_toolkit import SQL_PATH
from webapps.discovery_toolkit import discovery_toolkit_blueprint
########## Imports [ END]  ##########

########## @discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST']) [START] ##########
@discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST'])
def dashboard():
    fake = Faker()

    duns_branches = []
    gci_matches = []
    gci_no_matches = []
    for j in range(10):
        duns_branches.append(''.join(fake.random_uppercase_letter() for i in range(3)))
        gci_matches.append(fake.random_int(min=0, max=560, step=3))
        gci_no_matches.append(fake.random_int(min=0, max=560, step=4))

    response = {
        'global_engagement': {
            'account_name' : fake.company(),
            'account_id' : fake.bothify(text='C#######'),
            'is_new_logo' : ('Yes' if fake.boolean(chance_of_getting_true=25) else 'No'),
            'is_DNA' : ('Yes' if fake.boolean(chance_of_getting_true=60) else 'No'),
            'is_GNA' : ('Yes' if fake.boolean(chance_of_getting_true=50) else 'No'),
            'is_GTDP' : ('Yes' if fake.boolean(chance_of_getting_true=25) else 'No'),
            'is_ADP' : ('Yes' if fake.boolean(chance_of_getting_true=10) else 'No'),
            'is_Account_Management' : ('Yes' if fake.boolean(chance_of_getting_true=50) else 'No'),
        },
        'duns_location': {
            'total_gci_match' : fake.random_int(min=1000, max=3500,step=1),
            'total_locations' : fake.random_int(min=3500, max=5500,step=2),
            'chart':{
                'branches': duns_branches,
                'gci_matches': gci_matches,
                'gci_no_matches': gci_no_matches,
            },
        },
        'meetings_information': {
            'total_in_person_meetings': fake.random_int(min=0, max=345,step=5),
            'total_in_phone_web_meetings': fake.random_int(min=0, max=478,step=6),
            'total_won_opportunities': fake.random_int(min=0, max=150,step=7),
            'total_active_opportunities': fake.random_int(min=0, max=265,step=8),
            'total_on_hold_opportunities': fake.random_int(min=0, max=40,step=9),
            'total_lost_opportunities': fake.random_int(min=0, max=206,step=10),
        }
    }

    flash(message='Loading data',category='info')
    return render_template(APP_NAME + '/dashboard.html',response=response)
########## @discovery_toolkit_blueprint.route("/dashboard",methods=['GET','POST'])  [END]  ##########
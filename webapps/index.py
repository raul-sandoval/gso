########## Imports [START] ##########
from webapps import app
########## Imports  [END]  ##########

########## @app.route("/") route [START] ##########
@app.route("/")
def index():
    return 'home page'
########## @app.route("/") route  [END]  ##########

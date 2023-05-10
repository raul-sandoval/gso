########## Imports [START] ##########
from config import GSD_CNXSTR
from config import LOG_PATH
from config import VIZCRM_DATABASE
from config import VIZCRM_PASSWORD
from config import VIZCRM_PORT
from config import VIZCRM_SERVER
from config import VIZCRM_USERNAME
from sqlalchemy import *
import datetime
import pandas as pd
import pyodbc
import sqlalchemy
########## Imports  [END]  ##########

########## Global Variables [START] ##########

########## Global Variables  [END]  ##########

########## def gso_get(strQuery): [START] ##########
def gso_get(strQuery):
    df_input = pd.DataFrame()
    try:
        cnxn = pyodbc.connect(GSD_CNXSTR)  # returns connection object
        cursor = cnxn.cursor()
        df_input = pd.read_sql_query(strQuery, cnxn)
        cnxn.close()
    except Exception as e:
        fnLog('gso_get(strQuery)',strQuery,e.__str__())
        return e.__str__()
    return df_input
########## def gso_get(strQuery):  [END]  ##########

########## def gso_insert(strQuery): [START] ##########
def gso_insert(strQuery):
    try:
        cnxn = pyodbc.connect(GSD_CNXSTR)  # returns connection object
        cursor = cnxn.cursor()
        cursor.execute(strQuery)
        cnxn.commit()
        return 'success'
    except Exception as e:
        fnLog('gso_insert(strQuery)',strQuery,e.__str__())
        return e.__str__()
########## def gso_insert(strQuery):  [END]  ##########

########## def vizcrm_get(strQuery): [START] ##########
def vizcrm_get(strQuery):
    df_input = pd.DataFrame()
    vizcrm_username = VIZCRM_USERNAME
    vizcrm_password = VIZCRM_PASSWORD
    vizcrm_server = VIZCRM_SERVER
    vizcrm_database = VIZCRM_DATABASE
    vizcrm_port = VIZCRM_PORT
    try:
        con = sqlalchemy.create_engine(f"ibm_db_sa://{vizcrm_username}:{vizcrm_password}@{vizcrm_server}:{vizcrm_port}/{vizcrm_database}")
        df_input = pd.read_sql(strQuery, con)
    except:
        try:
            connection_uri = sqlalchemy.engine.URL.create(
                "ibm_db_sa",
                username=vizcrm_username,
                password=vizcrm_password,
                host=vizcrm_server,
                database=vizcrm_database,
            )
            con = create_engine(connection_uri)
            df_input = pd.read_sql(strQuery, con)
        except Exception as e:
            fnLog('vizcrm_get(strQuery)',strQuery,e.__str__())
            return pd.DataFrame()
    return df_input
########## def vizcrm_get(strQuery):  [END]  ##########


########## def fnLog(pFunction,pQuery,pError): [START] ##########
def fnLog(pFunction,pQuery,pError):
    actual_date = datetime.datetime.now()
    actual_date = actual_date.strftime("%m/%d/%Y %H:%M:%S")
    file_object = open(LOG_PATH + 'databases.txt', 'a')
    file_object.write("########## " + actual_date + " [START] ##########" + "\n")
    file_object.write("\t function: " + pFunction + "\n")
    file_object.write("\t Query:" + "\n")
    file_object.write("----------" + "\n")
    file_object.write(pQuery + "\n")
    file_object.write("----------" + "\n")
    file_object.write("\t Error message: " + pError + '\n')
    file_object.write("########## " + actual_date + "  [END]  ##########" + "\n\n")
    file_object.close()
########## def fnLog(pFunction,pQuery,pError):  [END]  ##########
from os import getenv
from json import loads

def get_db_connection_config()->dict:
    return dict(loads(getenv('authdb_config')))


with open('db_utils/update_token.sql') as f:
    update_sql_query = f.read()



def get_google_config()->dict: 
    res={} 
    res['scopes']=loads(getenv('google_scopes'))
    res['redirect_uri']=getenv('redirect_url')
    res['secret']=getenv('google_token_path')    
    return res



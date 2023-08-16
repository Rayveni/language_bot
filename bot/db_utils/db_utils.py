from os import getenv
from json import loads

def get_db_connection_config()->dict:
    return dict(loads(getenv('authdb_config')))

def get_google_config()->dict: 
    res={} 
    res['scopes']=loads(getenv('google_scopes'))
    res['redirect_uri']=getenv('redirect_url')
    res['secret']=getenv('google_token_path')    
    return res

def get_sql_queries()->dict:
    res={}
    with open('db_utils/user_info.sql') as f:
        res['user_info'] = f.read()
    with open('db_utils/upsert_user.sql') as f:
        res['upsert_user'] = f.read()        
    return res
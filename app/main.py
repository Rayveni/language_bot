from typing import Union

from os import getenv
from fastapi import FastAPI
from fastapi.requests import Request

import sys
sys.path.append("..")
from external_libs.db_manager import db_manager
from external_libs.google_api import google_auth
from db_utils import get_db_connection_config,get_google_config,update_sql_query

db_conn_config,update_query,google_config=get_db_connection_config(),update_sql_query,get_google_config()

                  
_google=google_auth(google_config['scopes'])  
google_auth_flow=_google.create_flow(google_config['secret'],google_config['redirect_uri'])


app = FastAPI()
@app.get("/callback")
async def auth2(request: Request,state: str):  

    authorization_response = str(request.url)
    # OAuth 2.0 should only occur over https.
    authorization_response = authorization_response.replace("http", "https")

    google_auth_flow.fetch_token(authorization_response=authorization_response)  
    db_conn=db_manager(**db_conn_config)
    data=await db_conn.run_sql_query(update_query,[state,_google.flow_json_credentials(google_auth_flow)],execute=True)
    return data

@app.get("/auth")
async def read_root():
    return google_auth_flow.authorization_url()[0]

@app.get("/test_api2")
async def qq(request: Request,state: int):

    return  state



@app.get("/")
def external_url(request:Request):
    return  str(request.url)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": get_db_connection_config()}
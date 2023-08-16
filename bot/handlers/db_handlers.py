from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db_utils import get_sql_queries,get_db_connection_config,get_google_config

import sys
sys.path.append("..")
from external_libs.db_manager import db_manager
from external_libs.google_api import google_auth



router = Router()


@router.message(Command("user_auth"))  
async def echo_handler(message: Message) -> None:
    
    user_id=message.from_user.id
    db_conn_config,sql_queries,google_config=get_db_connection_config(),get_sql_queries(),get_google_config()
    _google=google_auth(google_config['scopes'])  
    
    db_conn=db_manager(**db_conn_config)
    data=await db_conn.run_sql_query(sql_queries['user_info'],[user_id])
    if len(data)==0:
        google_auth_flow=_google.create_flow(google_config['secret'],google_config['redirect_uri'])
        authorization_url, state = google_auth_flow.authorization_url(
            # Enable offline access so that you can refresh an access token without
            # # re-prompting the user for permission. Recommended for web server apps.
            access_type='offline',
            # Enable incremental authorization. Recommended as a best practice.
            include_granted_scopes='true')
        db_conn=db_manager(**db_conn_config)
        data=await db_conn.run_sql_query(sql_queries['upsert_user'],[user_id,state],execute=True)
        
        res= authorization_url
    else:
        res=' data exists'

    await message.answer(res)
    
    

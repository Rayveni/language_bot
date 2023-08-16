from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from os import path

class google_auth:
    creds,service=None,None
    scopes:list=[]
    api_version:str='v4'
    
    def __init__(self, scopes:list):
        self.scopes=scopes
        #self.create_user_token(secret_file_path,user_token_path,register_server_port)
        #self.service=build('sheets', 'v4', credentials=self.creds)
        
    def create_flow(self, secret_file_path:str,redirect_uri:str):
        flow = InstalledAppFlow.from_client_secrets_file(secret_file_path, self.scopes)
        flow.redirect_uri=redirect_uri
        return flow       
    
    def flow_json_credentials(self, flow)->str:
        return flow.credentials.to_json()        
    
    def create_user_token(self, secret_file_path:str,user_token_path:str):
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.        

        if path.exists(user_token_path):
            self.creds = Credentials.from_authorized_user_file(user_token_path, self.scopes)
       
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else: 
                flow = InstalledAppFlow.from_client_secrets_file(secret_file_path, self.scopes)
                flow.redirect_uri=r'http://localhost:5001/callback'
                return flow.authorization_url()
                #self.creds = flow.run_local_server(open_browser=False)#port=register_server_port
            # Save the credentials for the next run
            with open(user_token_path, 'w') as token:
                token.write(self.creds.to_json())
                Credentials.from_authorized_user_info

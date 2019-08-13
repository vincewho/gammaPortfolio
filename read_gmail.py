from __future__ import print_function
import pickle
import os.path
import base64
import pandas as pd

from io import StringIO
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
credPath = r"C:\Users\VIN2164329\Downloads\google_api-master\credentials.json"
GMAIL_CREDENTIALS_PATH = credPath
GMAIL_TOKEN_PATH = "token.json"
search_query = "label:report-burn new burn"


def main():
    """
    Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credPath, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    
    # new_service = gmail.get_gmail_service(GMAIL_CREDENTIALS_PATH, GMAIL_TOKEN_PATH)
    new_results = service.users().messages().list(userId='me', q=search_query).execute()
    msgs = new_results['messages']
    msg_ids = [msg['id'] for msg in msgs]
    prefix=""
    for msg in msg_ids:
        messageId = msg
        new_msg = service.users().messages().get(userId='me', id=messageId).execute()
        parts = new_msg.get('payload').get('parts')
        all_parts = []
        
        for part in new_msg['payload']['parts']:
            if part['filename']:
                if 'data' in part['body']:
                    data = part['body']['data']
                else:
                    att_id=part['body']['attachmentId']
                    att=service.users().messages().attachments().get(userId='me', messageId=messageId,id=att_id).execute()
                    data=att['data']
                file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
                path = prefix+part['filename']

                with open(path, 'wb') as f:
                    f.write(base64.urlsafe_b64decode(data.encode('UTF-8')))

if __name__ == '__main__':
    main()
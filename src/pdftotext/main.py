import os
import pickle
import sys
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def drive_auth():
    # authentication 
    creds = None
    if os.path.exists('token.pickle'): # session check
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credential.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds), creds


def convert_pdf_to_text(input_file, output_txt):
    service, creds = drive_auth()
    file_id = None

    try:
        file_metadata = {'name': os.path.basename(input_file),'mimeType': 'application/vnd.google-apps.document'}
        media = MediaFileUpload(input_file, mimetype='application/pdf', resumable=True)
        
        uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        file_id = uploaded_file.get('id')
        print(f"File uploaded successfully. File ID: {file_id}")
        #retrieving export link
        file_info = service.files().get(fileId=file_id, fields='exportLinks').execute()
        export_links = file_info.get('exportLinks', {})
        export_url = export_links.get('text/plain')
        
        # download via http get
        headers = {'Authorization': f'Bearer {creds.token}'}
        response = requests.get(export_url, headers=headers, stream=True)
        
        if response.status_code == 200:
            with open(output_txt, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                        f.write(chunk)
            print(f"Success! Saved to {output_txt}")
            
        else:
            raise Exception(f"Download failed with status code: {response.status_code}")

    except HttpError as error:
        print(f"An HTTP error occurred: {error}") #API error
    except Exception as e:
        print(f"An error occurred: {e}")
       
if __name__ == "__main__":
    convert_pdf_to_text(sys.argv[1], 'output.txt')
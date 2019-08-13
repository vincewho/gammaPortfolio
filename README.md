# downloadGmailAttachments
DownloadGmailAttachment was created because I could not find an up to date reference to download gmail attachments. I pulled information from the following stackoverflow posts:</p>

[download-a-csv-file-from-gmail-using-python](https://stackoverflow.com/questions/41749236/download-a-csv-file-from-gmail-using-python)

You will need to turn on the gmail api and download the credentials.json file to work with your account

[enable-gmail-api](https://developers.google.com/gmail/api/quickstart/python)

# Requirements
google-api-python-client\
io\
oauth2client\
os.path\
pandas\
pickle\

# Usage 
    # modify these scopes, delete the file token.pickle
    credPath = "path to credentials.json file"
    search_query = "your search term"






'''
TODO:
upload and parse characters made in google sheets to character pool
stuff to use:
https://github.com/burnash/gspread
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_api_secret.json, scope')
client = gspread.authorize(creds)

sheet = client.open('Character Sheet Concept')


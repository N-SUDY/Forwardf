from os import environ

API_ID = int(environ.get('API_ID', '11973721'))
API_HASH = environ.get('API_HASH', '5264bf4663e9159565603522f58d3c18')
BOT_TOKEN = environ.get('BOT_TOKEN', '6078234170:AAGX4CDjIN2owsTeYTFOzk47XACzFO1nZSA')
OWNER = int(environ.get('OWNER', '1391556668'))
FILE_CAPTION = environ.get('FILE_CAPTION', '<b>{file_name}</b>')
TARGET_DB = int(environ.get("TARGET_DB", '-1001849017994'))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1001821439025'))
PORT = int(environ.get("PORT", "8080"))

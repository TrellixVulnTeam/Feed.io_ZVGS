import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('../Credentials/GDrive.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Feedsse.io Data sheet').sheet1

pp = pprint.PrettyPrinter()
res = sheet.row_values(2)
pp.pprint(res)
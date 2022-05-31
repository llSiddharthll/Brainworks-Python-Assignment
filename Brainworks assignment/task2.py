import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("brainworks-task2.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Brainworks task2").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

n = int(input("enter the number of strings you want to insert :"))

for i in range(1,n+1):
    a = input("enter the string : ")
    insertRow = [a]
    sheet.insert_row(insertRow,i)

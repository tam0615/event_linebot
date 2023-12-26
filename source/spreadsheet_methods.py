import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

#Set credential file in JSON
SPREADSHEET_KEY = os.environ["SPREADSHEET_KEY"]
json_file = "./eventlinebot-de30cdb54d0b.json" ##Your Credential
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
gc = gspread.authorize(credentials)


def GetWorksheets():
    workbook = gc.open_by_key(SPREADSHEET_KEY)
    worksheet_name=[]
    worksheet_list = workbook.worksheets()
    for i in range(len(worksheet_list)):
        worksheet_name.append(worksheet_list[i].title)
    sheet_dict = dict(zip(worksheet_name, worksheet_list))
    return sheet_dict

def ConvertPandas(worksheet):
    return pd.DataFrame(worksheet.get_all_values()[1:], columns=worksheet.get_all_values()[0])

def GetCell(worksheet, row, col):
    return worksheet.cell(row, col).value

def GetCol(worksheet, col):
    return worksheet.col_values(col)

def CountRow(worksheet, row):
    return len(worksheet.row_values(row))

def UpdateCell(worksheet, row, col, data):
    worksheet.update_cell(row, col, data)

def AppendRow(worksheet, row):
    worksheet.append_row(row)

def DeleteRow(worksheet, row):
    worksheet.delete_row(row)

def FindAndGetRowNum(worksheet, value):
    return worksheet.find(value).row
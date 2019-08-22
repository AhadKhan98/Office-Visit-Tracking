"""

This program is built for the Labor Office at Berea College. The purpose of this program
is to utilize a barcode scanner to scan for student id numbers and find information such as
full name, date of birth, reason for visit. The information is then saved into a spreadsheet
in the labor program's smartsheet account.
@author: Ahad Zai

"""

import os
from simple_smartsheet import Smartsheet
from simple_smartsheet.models import Sheet, Column, Row, Cell, ColumnType

api_token = "Enter Token Here"
smartsheet = Smartsheet(api_token)

def setup_smartsheet():
    sheets =  smartsheet.sheets.list()

    # Create a list containing only the sheet names and not ids
    sheet_names = []
    for s in sheets:
        sheet_names += [s.name]

    sheet_name = "Office Visit Tracking Program"

    # Check if sheet already exists, if not then add if yes then do nothing
    if sheet_name not in sheet_names:
        sheet_skeleton = Sheet(
        name=sheet_name,
        columns=[
        Column(title='Date',type=ColumnType.TEXT_NUMBER),
        Column(primary=True,title='B#',type=ColumnType.TEXT_NUMBER),
        Column(title='First Name',type=ColumnType.TEXT_NUMBER),
        Column(title='Last Name',type=ColumnType.TEXT_NUMBER),
        Column(title='Reason for Visit',type=ColumnType.TEXT_NUMBER),
        Column(title='Other',type=ColumnType.TEXT_NUMBER),
        Column(title='Labor Department',type=ColumnType.TEXT_NUMBER),
        ],
        )
        result = smartsheet.sheets.create(sheet_skeleton)

    return smartsheet.sheets.get('Office Visit Tracking Program')


def main():
    sheet = setup_smartsheet()
    sheet_name = sheet.name
    sheet_id = sheet.id

    to_add = Row(to_top=True,cells=
    [
    Cell(column_id=sheet.get_column("Date").id,value="12/30/1998"),
    Cell(column_id=sheet.get_column("B#").id,value="B00727232"),
    Cell(column_id=sheet.get_column("First Name").id,value="Ahad"),
    Cell(column_id=sheet.get_column("Last Name").id,value="Zai"),
    Cell(column_id=sheet.get_column("Reason for Visit").id,value="Direct Deposit"),
    Cell(column_id=sheet.get_column("Other").id,value="If possible"),
    Cell(column_id=sheet.get_column("Labor Department").id,value="Labor Office")
    ])

    smartsheet.sheets.add_row(sheet_id,to_add)


if __name__=="__main__":
    main()

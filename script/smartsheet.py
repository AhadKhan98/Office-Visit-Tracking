import os
from simple_smartsheet import Smartsheet
from simple_smartsheet.models import Sheet, Column, Row, Cell, ColumnType

api_token = "API TOKEN HERE"
smartsheet = Smartsheet(api_token)

class Smartsheet:

    def setup(self):
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

    def add_entry(self,entry_date,entry_bnum,entry_fname,entry_lname,entry_reason,entry_other,entry_department):
        sheet = self.setup()
        sheet_name = sheet.name
        sheet_id = sheet.id
        to_add = Row(to_top=True,cells=
        [
        Cell(column_id=sheet.get_column("Date").id,value=entry_date),
        Cell(column_id=sheet.get_column("B#").id,value=entry_bnum),
        Cell(column_id=sheet.get_column("First Name").id,value=entry_fname),
        Cell(column_id=sheet.get_column("Last Name").id,value=entry_lname),
        Cell(column_id=sheet.get_column("Reason for Visit").id,value=entry_reason),
        Cell(column_id=sheet.get_column("Other").id,value=entry_other),
        Cell(column_id=sheet.get_column("Labor Department").id,value=entry_department)
        ])
        smartsheet.sheets.add_row(sheet_id,to_add)

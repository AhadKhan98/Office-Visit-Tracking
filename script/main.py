"""

This program is built for the Labor Office at Berea College. The purpose of this program
is to utilize a barcode scanner to scan for student id numbers and find information such as
full name, date of birth, reason for visit. The information is then saved into a spreadsheet
in the labor program's smartsheet account.
@author: Ahad Zai

"""

import os
import time
from datetime import date
from smartsheet import Smartsheet

def get_information():
    date_today = date.today()
    bnum = input("Enter B#: ")
    fname = "Ahad"
    lname = "Zai"
    reason = "Direct Deposit"
    other = "Other Reason"
    department = "Labor Program Office"
    return date_today,bnum,fname,lname,reason,other,department

def main():
    sheet = Smartsheet()
    sheet.setup()
    while True:
        date_today,bnum,fname,lname,reason,other,department = get_information()
        sheet.add_entry(date_today,bnum,fname,lname,reason,other,department)
        time.sleep(0.5)

if __name__=="__main__":
    main()

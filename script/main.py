"""

This program is built for the Labor Office at Berea College. The purpose of this program
is to utilize a barcode scanner to scan for student id numbers and find information such as
full name, reason for visit. The information is then saved into a spreadsheet
in the labor program's smartsheet account.
@author: Ahad Zai

"""

import os
import time
from datetime import date
from smartsheet import Smartsheet
from gui import GUI
from tkinter import *


def structure_data(data):
    date_today = date.today()
    bnum = data[0]
    fname = data[1]
    lname = data[2]

    reasons = ''
    if data[3] == 1:
        if reasons == '':
            reasons += 'Direct Deposit'
        else:
            reasons += ',Direct Deposit'
    if data[4] == 1:
        if reasons == '':
            reasons += 'Paycheck'
        else:
            reasons += ',Paycheck'
    if data[5] == 1:
        if reasons == '':
            reasons += 'Pay Stubs'
        else:
            reasons += ',Pay Stubs'
    if data[6] == 1:
        if reasons == '':
            reasons += 'Paperwork for external partners'
        else:
            reasons += ',Paperwork for external partners'
    if data[7] == 1:
        if reasons == '':
            reasons += 'Clock-In Issue'
        else:
            reasons += ',Clock-In Issue'
    if data[8] == 1:
        if reasons == '':
            reasons += 'Other'
        else:
            reasons += ',Other'
    other_reason = data[9]

    return date_today,bnum,fname,lname,reasons,other_reason

def main():
    sheet = Smartsheet()
    sheet.setup()
    while True:
        form_instance = GUI()
        customer_data = form_instance.setup()
        date_today,bnum,fname,lname,reasons,other_reason = structure_data(customer_data)
        sheet.add_entry(date_today,bnum,fname,lname,reasons,other_reason)


if __name__=="__main__":
    main()

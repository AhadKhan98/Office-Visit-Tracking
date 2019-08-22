"""

This program is built for the Labor Office at Berea College. The purpose of this program
is to utilize a barcode scanner to scan for student id numbers and find information such as
full name, date of birth, reason for visit. The information is then saved into a spreadsheet
in the labor program's smartsheet account.
@author: Ahad Zai

"""

import os

from smartsheet import Smartsheet


def main():
    sheet = Smartsheet()
    sheet.setup()
    sheet.add_entry('date','bnum','fname','lname','resason','other','department')


if __name__=="__main__":
    main()

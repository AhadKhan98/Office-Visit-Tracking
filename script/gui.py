from tkinter import *

class GUI:


    def setup(self):
        window = Tk()

        window.title("Office Tracking")

        # Title Label
        title_label = Label(window,text="Office Visit Tracking")
        title_label.grid(row=1,column=0)


        # B# Label
        bnum_label = Label(window,text="B#:")
        bnum_label.grid(row=2,column=0)


        # B# Entry
        bnum_entry = Entry(window)
        bnum_entry.grid(row=2,column=1)

        # First Name Label
        first_name_label = Label(window,text="First Name:")
        first_name_label.grid(row=3,column=0)


        # First Name Entry
        first_name_entry = Entry(window)
        first_name_entry.grid(row=3,column=1)

        # Last Name Label
        last_name_label = Label(window,text="Last Name:")
        last_name_label.grid(row=4,column=0)


        # Last Name Entry
        last_name_entry = Entry(window)
        last_name_entry.grid(row=4,column=1)

        # Reason Label
        reason_label = Label(window,text="")
        reason_label.grid(row=5,column=0)
        reason_label = Label(window,text="Reason for Visit: ")
        reason_label.grid(row=6,column=0)




        window.mainloop()



gui = GUI()
gui.setup()

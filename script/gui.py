from tkinter import *

class GUI:


    def setup(self):
        window = Tk()

        window.title("Office Tracking")

        # Title Label
        title_label = Label(window,text="Office Visit Tracking")
        title_label.grid(row=0,column=1,sticky=W)
        blank_label = Label(window,text="")
        blank_label.grid(row=1,sticky=W)

        # B# Label
        bnum_label = Label(window,text="B#:")
        bnum_label.grid(row=2,sticky=W)


        # B# Entry
        bnum_entry = Entry(window)
        bnum_entry.grid(row=2,column=1)

        # First Name Label
        first_name_label = Label(window,text="First Name:")
        first_name_label.grid(row=3,sticky=W)


        # First Name Entry
        first_name_entry = Entry(window)
        first_name_entry.grid(row=3,column=1)

        # Last Name Label
        last_name_label = Label(window,text="Last Name:")
        last_name_label.grid(row=4,sticky=W)


        # Last Name Entry
        last_name_entry = Entry(window)
        last_name_entry.grid(row=4,column=1)

        # Reason Label
        reason_label = Label(window,text="")
        reason_label.grid(row=5,sticky=W)
        reason_label = Label(window,text="Reason for Visit: ")
        reason_label.grid(row=6,column=0,sticky=W)

        # Reason checkboxes
        direct_deposit_var = IntVar()
        direct_deposit_checkbox = Checkbutton(window,text="Direct Deposit",variable=direct_deposit_var)
        direct_deposit_checkbox.grid(row=7,column=0,sticky=W)

        paycheck_checkbox = Checkbutton(window,text="Paycheck")
        paycheck_checkbox.grid(row=7,column=1,sticky=W)

        paystubs_checkbox = Checkbutton(window,text="Pay Stubs")
        paystubs_checkbox.grid(row=7,column=2,sticky=W)

        paperwork_checkbox = Checkbutton(window,text="Paperwork")
        paperwork_checkbox.grid(row=8,column=0,sticky=W)

        clockin_checkbox = Checkbutton(window,text="Clock In Issues")
        clockin_checkbox.grid(row=8,column=1,sticky=W)

        other_var = IntVar()
        def show_hide_other():
            if other_var.get() == 1:
                other_label.grid(row=9,column=0,sticky=W)
                other_entry.grid(row=9,column=1,sticky=W)
            else:
                other_label.grid_remove()
                other_entry.grid_remove()
        other_checkbox = Checkbutton(window,text="Other",variable=other_var,command=show_hide_other)
        other_checkbox.grid(row=8,column=2,sticky=W)


        other_label = Label(window,text="Other Reason:")
        other_entry = Entry(window)

        submit_button = Button(window,text="Submit",width=10)
        submit_button.grid(row=10,column=2)


        window.mainloop()




gui = GUI()
gui.setup()

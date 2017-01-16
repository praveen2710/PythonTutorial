from tkinter import *
from xml.dom.minidom import Entity

root = Tk()
##code in here
label1 = Label(root, text="Enter first name")
label2 = Label(root, text="Enter last name")

firstNameEntry = Entry(root)
lastNameEntry = Entry(root)

#when using grid we need not call pack function
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
firstNameEntry.grid(row=0, column=1)
lastNameEntry.grid(row=1, column=1)

root.mainloop()

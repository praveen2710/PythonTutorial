from tkinter import *

root = Tk()
##code in here
label1 = Label(root, text="First", bg="Blue", fg="white")
#fill helps to resize the widject based on window size
#X fills the width
label1.pack(fill=X)

#y fills height of window
label2 = Label(root, text="Second", bg="Red", fg="white")
label2.pack(side=LEFT, fill=Y)
root.mainloop()

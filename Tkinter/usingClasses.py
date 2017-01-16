from tkinter import *


class myButtons:

    def __init__(self,rootone):
        frame1 = Frame(rootone)
        frame1.pack()

        self.printButton = Button(frame1, text="click to View", command=self.displayString)
        self.printButton.pack()
        self.exitButton = Button(frame1,text="click to exit",command=frame1.quit)
        self.exitButton.pack(side=LEFT, fill=Y)

    def displayString(self):
        print("print this string when button clicked")

root = Tk()
mButton = myButtons(root)
mButton
##code in here
root.mainloop()

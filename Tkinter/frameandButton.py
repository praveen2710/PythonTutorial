from tkinter import *

root = Tk()

#Creating frame and attaching it to window
newFrame = Frame(root)
newFrame.pack()

#Creating frame and attaching it to window
otherFrame = Frame(root)
#this puts frame on bottom of winodwo
otherFrame.pack(side=BOTTOM)

#created button on frame with text and color
button1 = Button(newFrame,text="Click here",fg="Red")

#created button on frame with text and color
button2 = Button(otherFrame,text="Click here",fg="Blue")

button1.pack()
button2.pack()

#pauses window for us to see and only closes it when we hit close button
root.mainloop()
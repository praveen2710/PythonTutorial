###User Interface to
###1)Add Button
###2)Add Menu Bar
###3)ToolBar
###4)Status Bar
###5)MessageBox
###6)Canvas

from tkinter import *
import tkinter.messagebox

root = Tk()
##code in here

##Adding Menu Bar
mymenu = Menu(root)
root.config(menu=mymenu)

fileSubMenu = Menu(mymenu)

mymenu.add_cascade(label="File",menu= fileSubMenu)

def newProjectWindow():
    print("lets create a new menu")

def saveCurrentProject():
    print("lets create a new menu")

fileSubMenu.add_command(label="New Project",command=newProjectWindow)
fileSubMenu.add_command(label="Save",command=saveCurrentProject)

fileSubMenu.add_separator()

#never pass in () after calling method like root.quit()
fileSubMenu.add_command(labe="exit",command=root.quit)

editSubMenu = Menu(mymenu)
mymenu.add_cascade(label="Edit",menu= editSubMenu)

def undoLastAction():
    print("Undo Last Action")

editSubMenu.add_command(labe="Undo",command=undoLastAction)

def doSomenthing():
    print("You clicked a button")

def insertHere():
    print("insert something here")

def printStuff():
    print("print something here")

##Adding toolbar
toolbar = Frame(root,bg="yellow")

insertButton = Button(toolbar,text="insert",command =insertHere)
insertButton.pack(side=LEFT,padx=2,pady=3)

printButton = Button(toolbar,text="print",command =printStuff)
printButton.pack(side=LEFT,padx=2,pady=3)

toolbar.pack(side=TOP,fill=X)

##Addin button with action
#definiton should be defined before we pass it in as command
button1 = Button(root,text="Click me for action",command=doSomenthing)
button1.pack()

def printStuff():
    return 'status back'


##Status Bar
#figure how to make text dynamic
statusBar = Label(root,text=printStuff,bd=1,relief=SUNKEN,anchor = W)
statusBar.pack(side=BOTTOM,fill = X)

##Message Box
tkinter.messagebox.showinfo("Title here","Message Here")


response = tkinter.messagebox.askquestion("Your Health","Yo you good")

if response == 'yes':
    print("He doing good")
else:
    print("Not so well")


root.mainloop()

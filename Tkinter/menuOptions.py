from tkinter import *

def function1():
    print("Menu item Project clicked")

def function2():
    print("Menu item Save clicked")

def function3():
    print("Edit Menu item undo clicked")

root = Tk()
myMenu = Menu(root)
root.config(menu=myMenu)
fileSubMenu = Menu(myMenu)

myMenu.add_cascade(label="File", menu=fileSubMenu)

fileSubMenu.add_command(label="Project", command=function1)
fileSubMenu.add_command(label="Save", command=function2)
fileSubMenu.add_separator()
fileSubMenu.add_command(label="exit", command=root.quit)

editMenu = Menu(myMenu)
myMenu.add_cascade(label="Edit",menu = editMenu)
editMenu.add_command(label="Undo",command=function3)

##code in here
root.mainloop()

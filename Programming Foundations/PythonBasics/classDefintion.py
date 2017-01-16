from tkinter import Scale


class Students:

    def __init__(self,name,contact):
        self.name = name
        self.contact = contact



    def getdata(self):
        print("Acceptind data")
        self.name = input("Enter name of student:")
        self.contact = input("Enter contact info:")

    def show_info(self):
        print("Students Name:"+self.name,"Contact info is"+self.contact)


class ScienceStudent(Students):

    def __init__(self,degree):
        self.degree = degree

    def science(self):
        print("I am science student of degree:"+self.degree)

#
# s1 = Students("blank","0")
# s1.getdata();
# s1.show_info();

Rob = ScienceStudent("M.Sc")
Rob.science()
Rob.getdata()
Rob.show_info()
###Encapsulation

##adding __ before a varialbe name makes it hidden
#__hiddenvariable

class Incrementer:
    #these variables are all used by one instance object of class
    __hiddenvariable = 0
    openVarialbe = 2

    def add(self,increment):
        self.__hiddenvariable += increment
        self.openVarialbe+= increment
        print(self.__hiddenvariable)
        return self.openVarialbe


add2 = Incrementer()
print(add2.add(2))
print (add2.openVarialbe)

add3 = Incrementer()
print (add3.add(3))
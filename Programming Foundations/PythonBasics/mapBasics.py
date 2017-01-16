###Map

##this allows us to do operations on list and not only on single numbers
def addTwo(x):
    return x+2

add2List = [10,20,30,40,50]
9
##this wont work
#print(addTwo(add2List))

#this is how it works for lists
result = list(map(addTwo,add2List))
print(result)

##combing map and lambda
result2 = list(map(lambda x:x+2,add2List))
print(result2)

##String fomatting
numbers = [4,5,6]
newString = "Numbers:{0},{1},{2}".format(numbers[0],numbers[1],numbers[2])
print(newString)

date = [12,13,2016]
dateString = "Date:{0}/{1}/{2}".format(date[0],date[1],date[2])
print(dateString)

a = "{x}/{y}".format(x=100,y=200)
print(a)

##join
print(":".join(["Apple","Banana","Mango"]))
##replace
#replace is case sensitive
print("Hello There".replace("There","World"))
newHeloBuddy = "Hello There"
#need to save the new string in some variable
newHeloBuddy = newHeloBuddy.replace("There","Buddy")
print(newHeloBuddy)

##startsWidth and endswith works with words
print(newHeloBuddy.startswith("Hello"))
print(newHeloBuddy.endswith("There"))

##upper and lower case
print(newHeloBuddy.upper())
print(newHeloBuddy.lower())
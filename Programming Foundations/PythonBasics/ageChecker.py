## example for if else

# age = int(input('Enter your age:'))
#
# if 18 <= age <= 50:
#     print('you are an young')
# elif age > 50:
#     print("your are old")
# elif age == 1 or age == 2:
#     print("this is toddler")
# else:
#     print('you are still a kid')

## example for lists
names = ["Mike","John","Rob"]
print(names)
print(names[2])

numbers = [3,5,7]
listSum = numbers[0]+numbers[2]
print(listSum)

abc = []

### Operations in list

##replace
numbers[2] = 9

print(numbers)

newnumbers = [2,4,6]

#adding two lists
print(numbers + newnumbers)

#repeating in list
print(numbers * 3)

##check if item exists in list
fruits = ["Mango","Peach","Apple"]
print("Apple" in fruits)
print("Orange" in fruits)

###Functions in list

##insert
numbers.insert(2,11)
numbers.append(13)

##size of list
print(len(numbers))

##location of item in list
print(numbers)
print(numbers.index(9))
print(fruits.index("Peach"))
### Range function and For Loop
##first 0-(n-1) numbers repeats n times
numbers = list(range(10))
print(numbers)

##with start and stop(the stop number is not included)
numbers = list(range(5, 19))
print(numbers)

##range between numbers (print even numbers
numbers = list(range(0, 31, 2))
print(numbers)

##list comprehension in use here to print square of even numbers
list = [x**2 for x in range(10) if x**2 % 2 == 0]

##for loop using range
# it repeats from 2 to 8
for x in range(2, 9):
    print(x)

print("second example")

# this repeats this from 0 - 10
for y in range(11):
    print(y)


def function1():
    print("pj")
    print("megha")


# example of repeating functions using range
for x in range(1, 4):
    function1()

fruits = ["Apple", "Banana", "Peach", "Orange"]

# example to print list
for fr in fruits:
    print(fr)

# for loop for even numbers
for x in range(0, 21, 2):
    print(x)

###While loop
count = 0
print("While Example")
while count < 10 or count == 10:
    print(count)
    count += 1

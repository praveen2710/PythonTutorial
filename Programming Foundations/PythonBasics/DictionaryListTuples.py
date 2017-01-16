####Section - 6

##List has [] dictionary has {} tuples has ()
numbers = [0,100,200,300,400,500,600]
people = {"john": 32, "Larry": 12, "Rob": 23}
#list comprehension in use here to print square of even numbers
list = [x**2 for x in range(10) if x**2 % 2 == 0]

##slicing lists,dictionary
#values startinf at 3 and before 5
print(numbers[3:5])
#values on left side before 3
print(numbers[:3])
#value on right hand side
print(numbers[3:])
#interval when slicing
print(numbers[1:6:2])

##tuples are immutable dictionary ie. once created cannot  be modified
fruits = ("Apple","Mango","Peach")
print(fruits[0])
veggies = "Cabbage","Spinach","Onions"
print(veggies[2])

##print value for key  Case Sensitive
print(people["john"])
print("Larry" in people)

##functions in dictionary
print(people.keys())
print(people.items())
#key and default value if not found
print(people.get("John","check name buddy"))

print(list)

for p in people:
    print(p)

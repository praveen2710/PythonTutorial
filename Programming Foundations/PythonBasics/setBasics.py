###Sets

##set has only 1 value  {} wheres dictionary has pairs in {key:value}
numbers = {1,2,3,4,5,5,6}
print(5 in numbers)

#duplicates get removed from set
print(numbers)

#adding to set
numbers.add(9)
print(numbers)

#removing from set
numbers.remove(4)
print(numbers)

setA = {1, 3, 8, 5}
setB = {2, 4, 5, 6, 7}
##union has all elemets on both set excluding duplicats
print(setA.union(setB))
print(setA | setB)

#intersection only has common elements of both set excluding duplicates
print(setA.intersection(setB))
print(setA & setB)

#difference takes one set and remove all elements that are present in another set
print(setA.difference(setB))
print(setA - setB)
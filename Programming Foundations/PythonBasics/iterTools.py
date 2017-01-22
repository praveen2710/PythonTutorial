from itertools import count,accumulate,takewhile

for i in count(3):
    print (i)

    if i >= 20:
        break

#creates list that is sum of all previos integers
numbers = list(accumulate(range(8)))

print (numbers)

#takewhile creates list that satisfies the function
print(list(takewhile(lambda x: x<=6,numbers)))
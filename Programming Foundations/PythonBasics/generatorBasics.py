###Generators

def function():
    counter =  0 ;
    while counter<5:
        yield counter
        counter += 1

for x in function():
    print(x)

#generator example to generate even numbers list
def evenNumberGenerator(x):

    for i in range(x):
        if i%2 == 0:
            yield i

print(list(evenNumberGenerator(101)))
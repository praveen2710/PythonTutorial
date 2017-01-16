###Functions and arguments

#function with arguments and returns parameter
def add(a,b):
    c = a+b
    return c

def sqaure(c):
    return c*c

def add_ten(x):
    return x+10;

##function calling a function
def twice(func, arg):
    return func(func(arg))

result = add(12,14)
print(result)

sqResult = sqaure(add(2,3))
print(sqResult)

##function passed as parameter
print(twice(add_ten,10))
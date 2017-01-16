def square(x):
    return  x**2

print(square(4))

##Above function written in lambda
result = (lambda x:x**2)(4)
print(result)
## another way to print no need to assing it to a variable
print((lambda x:x**2)(4))

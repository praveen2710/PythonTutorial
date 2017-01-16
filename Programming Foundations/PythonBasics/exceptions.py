###

#SyntaxError: invalid syntax<<def func1(a,b)>><<print(a+b>>
#NameError: name 'ab' is not defined<<print(ab)>>

def func1(a,b):
    print(a+b)
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Hey no zero's in input")
    finally:
        print("I always happen")
func1(12,1)



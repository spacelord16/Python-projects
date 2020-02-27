a=int(input("First_number"))
b=int(input("Second_number"))

def add(a,b):
    return a+b
print(add(a,b))

def sub(a,b):
    return a-b
print(sub(a,b))

def mult(a,b):
    return a*b
print(mult(a,b))

def div(a,b):
    return a/b
print(div(a,b))


def factorial(a,b):
    the_number = a = b
    b = 1
    while a > 1:
        b *= a
        a = a - 1
    print(the_number,"!","=", b)

print(factorial(a,b))



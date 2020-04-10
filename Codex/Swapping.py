a = int(input("Enter a number"))
b = int(input("Enter 2nd number"))


def swap(a, b):
    a, b = b, a
    return a, b


print(swap(a, b))

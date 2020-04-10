n = int(input("Enter a number"))


def fibonacci(number):
    a = 0
    b = 1
    if number < 0:
        print("Incorrect output")
    elif number == 0:
        return a
    elif number == 1:
        return b
    else:
        for i in range(2, number):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(n))

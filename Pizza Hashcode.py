def cutPizza(n):
    if 360 % n == 0:
        print("1", end=" ")
    else:
        print("0", end=" ")

    if n <= 360:
        print("1", end=" ")
    else:
        print("0", end=" ")

    if ((n * (n + 1)) / 2) <= 360:
        print("1", end="")
    else:
        print("0", end="")


n = int(input("Enter number"))
cutPizza(n)

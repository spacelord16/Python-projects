n = int(input("Enter number : "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(" * ", end="")
        elif j == int(i / 2) + (i % 2):
            print(" * " if i % 2 == 1 else " *", end="")
        else:
            print(" ", end="")
    print("")

def pascal(n):
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            print(c, end=" ")
            c = int(c * (line - i) / i)
        print(" ")


n = int(input("Enter number"))
pascal(n)

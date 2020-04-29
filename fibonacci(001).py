def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


num = int(input("Enter a number"))
if num <= 0:
    print("Enter valid positive number ")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(fib(i))

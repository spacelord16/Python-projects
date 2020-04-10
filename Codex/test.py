num = 1


def f():
    global num
    num = num - 3
    print(num)


f()
print(num)

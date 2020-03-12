def nestf1():
    x = 10

    def nestf2():
        nonlocal x
        x = 20

    print(x)
    nestf2()
    print(x)


nestf1()

n = int(input("Enter a number"))
prime = True


if n < 2:
    print("Unique")
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
        else:
            continue

if prime:
    print("Prime")
else:
    print("Composite")



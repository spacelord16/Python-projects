n = int(input("Enter a number"))


def productPrimefactor(n):
    product = 1

    for i in range(2, n + 1):
        if (n % i == 0):
            isPrime = 1

            for j in range(2, int(i / 2 + 1)):
                if (i % j == 0):
                    isPrime = 0

            if (isPrime):
                product = product * i
    return product


print(productPrimefactor(n))

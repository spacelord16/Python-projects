n=int(input("Enter number"))
def sum(n):
    if n==1:
        return 1
    else:
        return n**2+sum(n-1)
print(sum(n))

n=int(input("Enter a number"));
if n<2:
    print("Composite");
else:
    for i in range(2,n):
        if n%i==0:
            print("Composite");
            break;
        else:
            print("Number is Prime");
            break;


#n=5;
#fact=1;
#for i in range(1,n+1):
 #   fact=fact*i;

  #  print("The factorial of n is :");
   # print(fact);


def factorial(num):
    if num==1:
        return num;
    else:
        return num * factorial(num-1);


num=int(input("Enter a Number:"))
if num<0:
    print("Factorial cannot be found negative numbers");
elif num==0:
    print("Factorial of 0 is 1");
else :
    print("Factorial of",num,"is:",factorial(num));

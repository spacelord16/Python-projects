# def fibonacci():
#     num=int(input("How many numbers that generates ?:"));
#
#     i=1;
#     if num==0:
#         fib=[];
#     elif num==1:
#         fib=[1];
#     elif num==2:
#         fib==[1,1];
#     elif num>2:
#         fib=[1,1];
#         while i<(num-1):
#             fib.append(fib[i] + fib[i-1]);
#             i +=1;
#         return fib;
# print(fibonacci());
# input();


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    # Driver Program


print(Fibonacci(9))
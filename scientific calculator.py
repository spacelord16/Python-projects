"""INSTRUCTIONS"""

"""PRESS RUN
ENTER FIRST NUMBER 
CLICK ENTER BUTTON ON THE KEYBOARD 
ENTER OPERATOR 
CLICK ENTER BUTTON AGAIN
ENTER THE SECOND NUMBER 
CLICK ENTER"" 

FOR OPERATORS ENTER THE FOLLOWING

You can upper or lower case for operations
>>> + for addition
>>> - for subtraction
>>> * for multiplication
>>> / for division
>>> ^ for power 
>>> r for root
>>> % for modulus
>>> pie for Pie
>>> sin for sin(trig)
>>> cos for cos(trig)
>>> tan for tan(trig)
>>> ! for factorial
>>> ln for ln(natural log)
"""


print("First open the notepad and check the information about the operators")
import math
first_number=float(input())
op=input().lower()
second_number=float(input())

if op == "+":
    print(first_number,"+",second_number,"=", first_number + second_number)
elif op == "-":
    print(first_number,"-",second_number,"=", first_number - second_number)
elif op == "*":
    print(first_number,"*",second_number,"=", first_number * second_number)
elif op == "/":
    print(first_number,"/",second_number,"=", first_number/second_number)
elif op == "^":
    print(first_number,"^",second_number,"=",first_number**second_number)
elif op == "r":
    print(first_number,"root",second_number,"=", math.sqrt(second_number))
elif op == "%":
    print(first_number,"%",second_number,"=",first_number % second_number)

elif op =="!":
    the_number= first_number=second_number
    second_number=1
    while first_number > 1:
        second_number*=first_number
        first_number=first_number-1
    print("n!(",the_number,")=", second_number)
elif op == "sin":
    print("sin(",second_number,")=",math.sin(second_number))
elif op == "cos":
    print("cos(",second_number,")=",math.cos(second_number))
elif op == "tan":
    print("tan(" + str(second_number) + ")=",math.tan(second_number))
elif op == "pie" or op=="pi" :
    print("Pie =",math.pi)
elif op == "ln":
    print("ln(,",second_number,")=",math.log(second_number))
else:
    print("Incorrect operator")



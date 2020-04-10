print("Lets play a game")
print("You guys ready?")
print("Provide 3 numbers")
a = input('First number:')
b = input('Second number:')
c = input('Third number:')

if a > b + c:
    print(a)
elif c > a + b:
    print(c)
else:
    print(b)

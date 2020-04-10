name = input("Enter a name")
height_m =int(input("Enter height"))
weight_kg =int(input("Enter the weight "))

bmi = weight_kg/(height_m**2)
print("bmi:")
print(bmi)
if bmi < 25:
    print(name)
    print("is not oveweight ")
else :
    print(name)
    print("He is overweight")

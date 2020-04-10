def checkYear(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


year = 2000
if checkYear(year):
    print("Leap Year")
else:
    print("Not a Leap Year")

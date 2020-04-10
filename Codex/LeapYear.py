x = int(input("Enter a year"))
result = "Leap Year" if x % 400 == 0 else "Leap year" if x % 4 == 0 and x % 400 != 0 else "Non leap Year"
print(result)

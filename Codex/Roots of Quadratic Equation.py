import math

a, b, c = int(input("Enter first coefficient")), int(input("Enter Second coefficient")), int(
    input("Enter third coefficient"))
try:
    r1, r2 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a, (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
    print(r1, r2)
except ValueError:
    print("Imaginary roots")

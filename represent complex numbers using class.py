class Complex:
    def initializeComplex(self):
        self.realSide = int(input("Enter the real part"))
        self.imaginarySide = int(input("Enter the Imaginary part"))

    def display(self):
        print(self.realSide, "+", self.imaginarySide, "i", sep="")

    def sum(self, c1, c2):
        self.realSide = c1.realSide + c2.realSide
        self.imaginarySide = c1.imaginarySide + c2.imaginarySide


c1 = Complex()
c2 = Complex()
c3 = Complex()

print("Enter the first complex number: ")
c1.initializeComplex()
print("First Complex number is :", end="")
c1.display()

print("Enter the second complex number: ")
c2.initializeComplex()
print("Second Complex number is", end="")
c2.display()

print("Sum of two Complex number is", end="")
c3.sum(c1, c2)
c3.display()

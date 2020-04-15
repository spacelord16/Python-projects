class salesSystem:
    def __init__(self, customerid=101, name='', address='', pd='', p=0, avg_rt=33750, avg_GST=81000, a='', b='', c='', type=''):
        print("\n\n****Welcome to Purchase System****")

        self.customerid = customerid
        self.name = name
        self.address = address
        self.pd = pd
        self.p = p
        self.avg_rt = avg_rt
        self.avg_GST = avg_GST
        self.Car1 = a
        self.Car2 = b
        self.Car3 = c
        self.type = type

    def inputdata(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your Address:")
        self.pd = input("\nEnter Purchase Date:")
        print("Your customer id is:", self.customerid, "\n")

    def typeOfVehicle(self):
        print("Here are following models:")
        print("1. ---> Car1")
        print("2. ---> Car2")
        print("3. ---> Car3")

        y = int(input("Enter Your choice"))

        if y == 1:
            self.type = self.Car1 = "Car1"
        elif y == 2:
            self.type = self.Car2 = "Car2"
        elif y == 3:
            self.type = self.Car3 = "Car3"
        else:
            print("Invalid option")

        print("You have selected", self.type)

    def modelSelection(self):

        print("Here are the following models prices:")

        print("1. Car1   --->   Rs550000")
        print("2. Car2   --->   Rs450000")
        print("3. Car3   --->   Rs350000")

        x = int(input("Enter your choice"))

        if x == 1:
            print("You have opted for Car1")
            self.p = 550000
        elif x == 2:
            print("You have opted for Car2")
            self.p = 450000
        elif x == 3:
            print("You have opted for Car3")
            self.p = 350000
        else:
            print("Invalid option")

        print("Your Selected model price is", self.p, "\n")

    def dislayBill(self):
        print("****Total Purchase Bill****")
        print("Customer details")
        print("Customer id:", self.customerid)
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Customer Purchase date", self.pd)
        print("Customer Selected model is", self.type)
        print("Customer Selected model price is Rs", self.p)
        print("Your ExShowroom Price Rs", self.p)
        print("Additional Taxes Rs", self.avg_rt + self.avg_GST)
        print("Your Total Price is Rs", self.p + self.avg_rt + self.avg_GST)


def main():
    a = salesSystem()

    while 1:
        print("1. Enter Customer Data")
        print("2. Model Selection")
        print("3. Calculate total price")
        print("4. Display Bill")
        print("5. Exit")

        b = int(input("Enter your Choice:"))
        if b == 1:
            a.inputdata()
        if b == 2:
            a.typeOfVehicle()
        if b == 3:
            a.modelSelection()
        if b == 4:
            a.dislayBill()
        if b == 5:
            quit()


main()

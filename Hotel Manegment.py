class hotelFare:

    def __init__(self, rt='', s=0, r=0, name='', address='', cindate='', coutdate='', rno=101, a=1800):
        print("\n\n****WELCOME TO TAJ****")

        self.rt = rt
        self.s = s
        self.r = r
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your Name")
        self.address = input("\nEnter your address")
        self.cidate = input("\nEnter your Check in date")
        self.coutdate = input("\nEnter your Check out Date")
        print("Your room number:", self.rno, "\n")

    def roomrent(self):

        print("We have following room categories:")
        print("1. Ultra Deluxe----> 10000 rs")
        print("2. Super Deluxe----> 8000 rs")
        print("3. Deluxe      ----> 6000 rs")
        print("4. Regular     ----> 4000 rs")

        x = int(input("Enter you Choice "))

        n = int(input("Enter Duration"))

        if x == 1:
            print("You have opted for Ultra Deluxe Room")
            self.s = 10000 * n
        elif x == 2:
            print("You have opted for Super Deluxe Room")
            self.s = 8000 * n
        elif x == 3:
            print("You have opted for Deluxe room")
            self.s = 6000 * n
        elif x == 4:
            print("You have opted for Regular room")
            self.s = 4000 * n
        else:
            print("Please choose a room")

        print("Your room rent is =", self.s, "\n")

    def restaurentBill(self):
        print("*****WELCOME TO ANNAPURNA RESTAURANT")

        print("1. Breakfast Combo ----> 250rs ")
        print("2. Lunch Combo     ----> 400rs ")
        print("3. Dinner Combo    ----> 450rs ")
        print("4. Exit")

        while 1:
            c = int(input("Enter your Choice"))
            if c == 1:
                d = int(input("Enter quantity"))
                self.r = self.r + 250 * d
            elif c == 2:
                d = int(input("Enter quantity"))
                self.r = self.r + 400 * d
            elif c == 3:
                d = int(input("Enter quantity"))
                self.r = self.r + 450 * d
            elif c == 4:
                break
        print("Total food cost =Rs", self.r, "\n")

    def displayBill(self):
        print("****Hotel Bill****")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer Address:", self.address)
        print("Customer Check in date:", self.cindate)
        print("Customer Check out date:", self.coutdate)
        print("Customer room number:", self.rno)
        print("Your Room rent:", self.s)
        print("Your Food Bill", self.r)

        self.rt = self.s + self.r

        print("Your Total bill", self.rt)
        print("Additional Service charge", self.a)
        print("Your GrandTotal", self.rt + self.a, "\n")
        self.rno += 1


def main():
    a = hotelFare()
    while 1:
        print("1. Enter Customer Data")
        print("2. Calculate RoomRent")
        print("3. Calculate RestaurantBill")
        print("4. Show TotalBill")
        print("5. Exit")

        b = int(input("Enter your Choice"))
        if b == 1:
            a.inputdata()
        if b == 2:
            a.roomrent()
        if b == 3:
            a.restaurentBill()
        if b == 4:
            a.displayBill()
        if b == 5:
            quit()
main()

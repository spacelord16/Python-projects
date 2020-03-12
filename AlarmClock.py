import datetime

print(datetime.datetime.today().strftime("%H"))
print(datetime.datetime.today().strftime("%M"))
Hour = int(input("Enter a Hour:"))
Minutes = int(input("Enter a Minute:"))
while True:
    if Hour == int(datetime.datetime.today().strftime("%H")) and Minutes == int(
            datetime.datetime.today().strftime("%M")):
        print("Alarm Raised")
        break
    else:
        print("Alarm not Raised")
        break

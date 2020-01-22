import datetime;
print(datetime.datetime.today().strftime("%H"));
print(datetime.datetime.today().strftime("%M"));
hour=int(input("Enter a Hour:"));
minutes=int(input("Enter a Minute:"));
while True:
    if Hour==int(datetime.datetime.today().strftime("%H")) and Minute==int(datetime.datetime.today().strftime("%M")):
        print("Alarm Raised");
        break;
    else:
        print("Alarm not Raised");
        break;

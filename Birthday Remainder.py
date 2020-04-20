Dict = {}
while True:
    print("_____Birthday Adder_____\n")
    print("1.Show Birthday")
    print("2.Add to Birthday list")
    print("3.Exit")
    choice = int(input("Enter the choice\n"))
    if choice == 1:
        if len(Dict) == 0:
            print("Nothing to show")
        else:
            name = input("Enter name to look for birthday")
            birthday = Dict.get(name, "No data found")
            print(birthday)
    elif choice == 2:
        name = input("Enter Name")
        date = input("Enter Birth date")
        Dict[name] = date
        print("Birthday Added")
    elif choice == 3:
        print("======Exiting program========")
        break
    else:
        print("Choose a valid option")

print("Welcome to the ATM")
restart = 'Y'
chances = 3
balance = 10000
while chances >= 0:
    pin = int(input("Enter your 4 digit Pin : "))
    if pin == 1234:
        print('Your entered pin is correct')
        print('Press 1 to check your balance')
        print('Press 2 to withdraw cash')
        print('Press 3 to Return card\n')
        while restart not in ('n', 'NO', 'no', 'N'):

            option = int(input('What would you like to choose :'))
            if option == 1:
                print('Your balance is Rs', balance)
                restart = input('Would you like to go back ?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = 'y'
                withdrawl = float(input('How much would you like to withdraw? 10,20,50,100,200,500,20000 for other '
                                        'enter 1:'))

                if withdrawl in [10, 20, 50, 100, 200, 500, 2000]:
                    balance = balance - withdrawl
                    print('\nYour balance is now Rs', balance)
                    restart = input('Would you like to go back ?')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 50, 100, 200, 500, 2000]:
                    print('Invalid Amount,Please Re-try\n')
                    restart = 'y'
                elif withdrawl == 1:
                    withdrawl = float(input('Enter desired amount:'))
            elif option == 3:
                print('Please wait while your card is returned ....\n')
                print('Thank You')
            else:
                print('Please enter a correct number.\n')
                restart = 'y'
    elif pin != '1234':
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\n No more tries')
            break

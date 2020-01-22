def guess():
    i=0;
    j=100;
    m=50;
    counter=1;

    print("Guess a number");
    condition=input("Is your guess" + str(m) + "? (0 means its too low, 1 mean its your guess and 2 means its too high)");
    while condition != 1:
        counter += 1;
        if condition == 0:
            i= m + 1;
        elif condition == 2:
            j= m - 1 ;

        m = (i + j) / 2;
        condition =input("Is your guess"+ str(m) + "? (0 means its too low ,1 means its your guess and 2 means its too high)");
    print("It took",counter,"times to guess your number");
guess();

 

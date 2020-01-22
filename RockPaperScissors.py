user1= input("What is your name?");
user2= input("And your name?");
user1-Answer= input("do yo you want rock,paper or scissors?" , user1);
user2-Answer=input("do yo you want rock,paper or scissors?" , user2);

def compare(user1,user2):
    if user1==user2 :
        return("Its a tie!");
    elif user1== rock:
        if user2== scissors :
            return("Rocks wins!");
        else:
            return("paper wins!");
    
    elif user1== scissors:
        if user2== paper :
            return("scissors wins!");
        else:
            return("rocks wins!");

    elif user1== paper:
        if user2== rock :
            return("paper wins!");
        else:
            return("scisssors wins!");

    else:
        return("Invalid input! You have not entered rock,paper,scissor");


print(compare(user1-Answer,user2-Answer));

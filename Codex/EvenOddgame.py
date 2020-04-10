import random;


def even_odd(choice, fingers):
    human_choice = choice;
    human_fingers = fingers;
    if human_choice == "Even":
        computer_choice = "Odd";
    else:
        computer_choice = "Even";
    computer_finger = random.radint(0, 10);
    total = human_fingers + computer_finger;
    if total % 2 == 0:
        result = "Even";
    else:
        result = "Odd";
    if human_choice == result:
        print("Congrats..You win");
    else:
        print("Sorry the computer wins..");


even_odd("Even", 4);

import random

print("Calculate your Love percentage")
Input_1 = input("Your Name:")
Input_2 = input("Your Partner name:")
Boy = (len(Input_1))
Girl = (len(Input_2))
rnd = random.randint(1, 20)
percentage = 100 - (Boy * Girl) - rnd

print("Chances of true love together is " + str(percentage) + " %")

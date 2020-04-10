def Grade(Total_Percentage):
    if Total_Percentage >= 75:
        return "You are in division 1"
    elif Total_Percentage >= 65:
        return "You are in division 2"
    elif Total_Percentage >= 55:
        return "You are in division 3"
    elif Total_Percentage >= 40:
        return "You are in division 4"
    else:
        return "Fail"


print(Grade(int(input("Enter Total percentage"))))
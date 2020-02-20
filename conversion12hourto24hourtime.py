import re


def convert24(str1):
    if str1[:2] == "12":
        if str1[-2:] == "AM":
            return "00" + str1[2:-2]
        elif str1[-2:] == "PM":
            return str1[:-2]
    elif str1[-2:] == "AM":
        return str1[-2:]
    else:
        return str(int(str1[:2])+12) + str1[2:8]

input_str = input("Enter string in format HH:MM:SS AM/PM")

flag = True
match = ""
while flag:
    if len(re.findall("(0?[0-9]|1[0-2]):([0-5]?[0-9]|60):([0-5]?[0-9]|60)\s(([A]|[P])M)", input_str)) > 0:
        flag = False
        match = input_str

print(convert24(match))

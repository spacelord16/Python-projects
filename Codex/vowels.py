import re

Name = input("Enter a letter")
Name = Name[0]
Name = Name.lower()
if len(re.findall("a|e|i|o|u", Name)) > 0:
    print("vowel")
else:
    print("Consonant")

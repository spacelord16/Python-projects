import re
password = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])
    (?=.*[!@#$&*])
    (?=.*[0-9].*[0-9])
    (?=.*[a-z].*[a-z].*[a-z])
    .{10,}
    $
    )''', re.VERBOSE)

def passwordCheck():
    passw = input("Enter a password:")
    m = password.search(passw)
    if(not m):
        print("Weak Password")
        return False
    else:
        print("Strong Password")
        return True
passwordCheck()
# POINTS = 0
# CON = 0
# VOL = 0
# print("Welcome to the love calculator")
# Love1 = input("Please enter the first persons name\n")
# Love2 = input("Please enter the second persons name\n")
#
# L1 = (len(Love1))
# L2 = (len(Love2))
#
# S1 = (Love1[:1])
# S2 = (Love2[:1])
#
# if L1 == L2:
#     POINTS = POINTS + 20
#
# if S1 == "a" or "e" or "i" or "o" or "u":
#     POINTS = POINTS + 5
# else:
#     POINTS = POINTS + 2.5
# if S2 == "a" or "e" or "i" or "o" or "u":
#     POINTS = POINTS + 5
# else:
#     POINTS = POINTS + 2.5
#
# print(POINTS)


boy = input("Whats the boy's name:")
print(boy)
girl = input("Whats the girl's name:")
print(girl)
lovecount = 0


def heart(x):
    print("""
     LOVE METER:
                ___    ___
               (   \__/   )
                \ {0}%    /
                 \      /
                  \____/
""".format(x))


def lovechecker():
    consonants = 'qwrtypsdfghjklzxcvbnm'
    vowels = 'ueioa'
    lovecount = 0
    for vowels in boy:
        for vowels in girl:
            if vowels in boy and vowels in girl:
                lovecount += 2
    for consonants in boy:
        for consonants in girl:
            if consonants in boy and consonants in girl:
                lovecount + 1
    if len(boy) + len(girl) >= 25:
        lovecount -= lovecount
        print('Error:\n Dont type in surnames or random input')
    if lovecount > 100:
        lovecount = 100
    impossible = (1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97)
    enemies = (2, 10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98)
    shyness = (3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99)
    friends = (4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100)
    slightlove = (5, 13, 21, 29, 37, 45, 53, 61, 69, 77, 85, 93)
    deeplove = (6, 14, 22, 30, 38, 46, 54, 62, 70, 78, 86, 94)
    marriage = (7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87, 95)
    tilldeath = (8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96)
    if lovecount in impossible:
        print('\tTOTALLY HORRIBLE MATCH!!!')
        print("""
        \tIMPOSSIBLE
      {0} and {1} two will never be together, not even friends\n
      NEVER!!!
      """.format(boy, girl))
        lovecount = -100
    if lovecount in enemies:
        print("""
        \tENEMIES
       With {0} and {1} there is no chance for even the slightest bit of love, only hatred.
       """.format(boy, girl))
        lovecount = -5
    if lovecount in shyness:
        print("""
           \tSHYNESS
       {0} and {1} atleast have a chance, but its being hindered by both of them being shy.
       """.format(boy, girl))
        lovecount = 15
    if lovecount in friends:
        print("""
           \tFRIENDS
       {0} and {1} are meant to be friends, and will find romance with other people.
       """.format(boy, girl))
        lovecount = 20
    if lovecount in slightlove:
        print("""
           \tLSlIGHT LOVE
       With {0} and {1} there is a chance this two will fall in love, though there is also a great chance of break up.
       """.format(boy, girl))
        lovecount = 30
    if lovecount in deeplove:
        print("""
           \tDEEP LOVE
       {0} and {1} will probably last long, and are highly compatible.
       """.format(boy, girl))
        lovecount = 60
    if lovecount in marriage:
        print("""
               \tMARRIAGE
           {0}'s and {1}'s love can end up being really deep and end in wedding bells.
           """.format(boy, girl))

        lovecount = 80

    elif lovecount in tilldeath:
        print("""
               \tTILL DEATH
           {0} and {1} won't only get married, but they will live a happy life together. forever........
           """.format(boy, girl))

        lovecount = 100
    elif lovecount == 0:
        print("""
               \tUNKNOWN
          It is impossible to determine if {0} and {1} are compatible.
          TOO BAD!

      """.format(boy, girl))

    heart(lovecount)


lovechecker()
import webbrowser
import time
import random

while True:
    sites = random.choice(['google.co.in', 'youtube.com', 'amazon.com', 'instagram.com/_aditya_1612_/',
                           'facebook.com/aditya.deshpande.526438','mail.google.com/mail/u/0/#inbox',
                           'mail.google.com/mail/u/1/#inbox'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange()

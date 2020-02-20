import datetime
from time import sleep

while True:
    print(datetime.datetime.now().strftime("%H:%M"))
    sleep(5)

import pyqrcode

url =pyqrcode.create("www.google.co.in")
url.svg('uca-url.svg',scale=9)
print(url.terminal(quiet_zone=1))
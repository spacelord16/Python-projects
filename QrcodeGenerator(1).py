import pyqrcode

url =pyqrcode.create("www.google.com")
url.svg('uca-url.svg',scale=8)
print(url.terminal(quiet_zone=5))

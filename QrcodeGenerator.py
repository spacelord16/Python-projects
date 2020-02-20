import io

import pyqrcode

url =pyqrcode.create("https://www.google.co.in")

url.png('code.png', scale=9)

buffer = io.BytesIO()
url.png(buffer)

print("Done..Check you folder")

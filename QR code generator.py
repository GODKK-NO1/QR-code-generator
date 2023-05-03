print("done")

import pyqrcode

s = str(input("Enter the site for which you want to have QR code for: "))

url = pyqrcode.create(s)

url.svg("your's site.svg", scale=8)
import pyqrcode

print("done")

s = str(input("Enter the site for which you want to have QR code for: "))

url = pyqrcode.create(s)

url.svg("QR code.svg", scale=8)

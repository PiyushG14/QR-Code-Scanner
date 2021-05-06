import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode

qr = pyqrcode.create("https://www.hackershrine.com")
qr.png("test2.png", scale=6)

data = decode(Image.open('wikiqr.png'))
print(data[0][0].decode('utf-8'))

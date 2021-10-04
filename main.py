#You can add an additional package to this project named "pypng" if you want to save the qr code in a png format.....
#If you use a python IDE, it would be better

import pyqrcode
from pyqrcode import QRCode
  

s = "website link here"
  
url = pyqrcode.create(s)
  
url.svg("urpic.svg", scale = 8)
  
url.png('urpic.png', scale = 6)

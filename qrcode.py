#!/usr/bin/env python3

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

program=('''
#!/usr/bin/env python3
from tom import aeternum
date=1468246320
aeternum(date)
''')




qr=pyqrcode.create(program)
qr.png("natalie.png", scale=8)

d=decode(Image.open("natalie.png"))
print(d[0].data.decode("ascii"))

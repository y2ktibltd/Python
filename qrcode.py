#!/usr/bin/env python3
import pyqrcode
import png
from pyqrcode import QRCode
code="""
Thanks, 
Tom Bigham / Comptia A+, Linux+, Python PCEP
IT Systems Support Oracle Analyst - Groveport
Boar's Head Brand
GP Techs: 614.662.5300 Ext. 8000
Direct: 614.662.5300 Ext. 8148
Cell: 614-286-8072
'Never attribute to malice that which is adequately explained by a misunderstanding.'"""
image=pyqrcode.create(code)
image.png('qrsig.png',scale=6)

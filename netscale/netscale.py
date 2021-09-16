#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.80.91.154', 2001))
data = s.recv(4)
s.close()

print ("received data:"), data

#!/usr/bin/env python3
from multiprocessing import process, cpu_count
import socket
from math import sqrt

server="192.168.1.30"
port=9999

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((server,port))
message=s.recv(1024)
message=int(message)
s.close()
print(message)
print(type(message))

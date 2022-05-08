#!/usr/bin/env python3
from multiprocessing import process, cpu_count
import socket
from math import sqrt
from time import sleep

server="192.168.1.30"
port=9999

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((server,port))
        message=s.recv(1)
        message=int(message)
#        print(message)
#        print(type(message))
        s.close()
    except socket.error:
        print("Done")
        exit()

#!/usr/bin/env python3
import socket
from sys import argv
import time

try:
            num=int(argv[1])
except IndexError:
        print("Must type an integer value after command")
        exit()
except ValueError:
        print("Must type an integer value after command")
        exit()

server=socket.gethostname()
port=9999

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
print(f"Socket {port} Created")
s.bind((server,port))
print(f"Bound to {server}")
s.listen()
num_list=[_ for _ in range(1,num,2)]
i=0

while i<len(num_list):
    c,addr=s.accept()
    data=str(num_list[i])
    buff_len=16-len(data)
    buff="0"*buff_len
    send=buff+data
    c.send(send.encode('ascii'))
    i+=1
    c.close()

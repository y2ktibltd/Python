#!/usr/bin/env python3
import socket
from sys import argv
from time import time
from threading import Thread

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

def send_send(num_list):
    i=0
    while i<len(num_list):
        c,addr=s.accept()
        data=str(num_list[i])
        buff_len=9-len(data)
        buff="0"*buff_len
        send=buff+data
        c.send(send.encode('ascii'))
        i+=1
        c.close()

t1=Thread(target=send_send,args=(num_list,))
t2=Thread(target=send_send,args=(num_list,))
t3=Thread(target=send_send,args=(num_list,))
t4=Thread(target=send_send,args=(num_list,))
t5=Thread(target=send_send,args=(num_list,))
t6=Thread(target=send_send,args=(num_list,))
t7=Thread(target=send_send,args=(num_list,))
t8=Thread(target=send_send,args=(num_list,))
start=time()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

stop=time()
total_time=stop-start
print(f"{total_time} seconds elapsed")

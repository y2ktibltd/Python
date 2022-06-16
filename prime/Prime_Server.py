#!/usr/bin/env python3
import socket
from sys import argv
from time import time
from multiprocessing import Process
from threading import Thread
import os

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
''' TO DO. SPLIT NUM_LST INTO EQUAL PARTS THEN SEND IN ONE BIG CHUNK TO TRY TO SPEEDUP PROGRAM
for a in range(len(num_lst)):
    for i in range(os.cpu_count()):
        num_list[i].append(num_lst[a])
exit()
'''
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

processes=[]
threads=[]
start=time()

for i in range(os.cpu_count()):
    print(f"Registering thread {i}")
    threads.append(Thread(target=send_send,args=(num_list,)))
for i in range(os.cpu_count()):
    print(f"Registering process {i}")
    processes.append(Process(target=send_send,args=(num_list,)))

for process in processes:
    process.start()
for thread in threads:
    thread.start()
for process in processes:
    process.join()
for thread in threads:
    thread.join()

stop=time()
total_time=stop-start
print(f"{total_time} seconds elapsed")

#!/usr/bin/env python3
import socket
from sys import argv
from time import time,sleep
from multiprocessing import Process
from threading import Thread
import numpy as np
import os


try:
    num=1000
    #num=int(argv[1])           #This is the default method for obtaining input from user
    max_clients=8
    #max_clients=int(argv[2])   #This is the defaulkt method of obtaining max_clients from user
except:
    print('''\nERROR:Command must be followed by how many integers to check for prime and number of clients.\n
      Example: ./Prime_Server 10000 10    
                              int   clients\n''')
    exit()

def Server_Start(num,max_clients):
    clients=0
    num_list=Create_Lists(num,max_clients)
    while clients<max_clients:
        server=socket.gethostname()
        port=9999
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((server,port))
        print(f"Bound to {server} on {socket.gethostbyname(server)}:{port}")
        print(f"{clients}/{max_clients}:Clients Connected")
        #s.listen()
        sleep(1)
        os.system('clear')


def Create_Lists(num,max_clients):
    nums=[_ for _ in range(1,num,2)]                        #Create initial list of odd numbers
    for i in range((max_clients-(len(nums)%max_clients))+max_clients):
       nums=np.append(nums,"EOF")                               #add 1's to end of array so numpy split is even
    num_list=np.reshape(nums,(max_clients,-1),order='F')    #use numpy to deal into 2D list*max_clients
    return num_list

def Client_Send(num_list,max_clients):
    i=0
    while i<max_clients:
        #c,addr=s.accept()
        #data=str(num_list[i])
        #buff_len=9-len(data)
        #buff="0"*buff_len
        #send=buff+data
        c.send(num_list[i].encode('ascii'))
        i+=1
        c.close()

Server_Start(num,max_clients)

num_list=Create_Lists(num,max_clients)

for i in range(max_clients):
    print(num_list[i],len(num_list[i]))


exit()




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

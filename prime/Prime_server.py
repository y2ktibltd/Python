#!/usr/bin/env python3
from multiprocessing import process, cpu_count
import socket
from math import sqrt
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
client_num=8
port=9999

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(f"Socket {port} Created")
s.bind((server,port))
print(f"Bound to {server}")
s.listen(client_num)
num_list=[_ for _ in range(2,num,2)]
i=0

while i<len(num_list):
    c,addr=s.accept()
    print(f"Sent {num[i]} to {addr}")
    c.sendall(str(num_list[i]).encode('ascii'))
    i+=1
    c.close()

#start_time=time.time()
#primes=[2]
#numbers=[_ for _ in range(2,num,2)]

"""
def isPrime(num):
    for i in range(3,num,2):
        for j in range(3,int(sqrt(i)+1),2):
            if i%j==0:
                break
        else:
            primes.append(i)
isPrime(num)
stop_time=time.time()
print (primes)
print("--- %s seconds ---" % (stop_time-start_time))
"""

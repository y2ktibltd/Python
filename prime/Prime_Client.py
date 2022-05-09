#!/usr/bin/env python3
from multiprocessing import process, cpu_count
import socket
from math import sqrt

server="192.168.1.30"
port=9999
primes=[]

def isPrime(num):
    for i in range(3,num,2):
        for j in range(3,int(sqrt(i)+1),2):
            if i%j==0:
                break
        else:
            primes.append(i)

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((server,port))
        num=s.recv(128)
        isPrime(int(num))
        s.close()
    except socket.error:
        print("Done")
        print(primes)
        exit()

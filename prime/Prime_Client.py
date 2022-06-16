#!/usr/bin/env python3
from multiprocessing import process, cpu_count
import socket
from math import sqrt
from multiprocessing import Process
from threading import Thread
import os

server="192.168.1.42"
port=9999
primes=[]

def isPrime(num):
        for j in range(3,int(sqrt(num)+1),2):
            if num%j==0:
                break
        else:
            primes.append(num)

def receive_numbers():
    while True:
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((server,port))
            num=s.recv(16)
            num=int(num)
            isPrime(num)
            s.close()
        except socket.error:
            print("Done")
            print(primes)
            exit()

processes=[]
threads=[]

for i in range(os.cpu_count()):
    processes.append(Process(target=receive_numbers))
for i in range(os.cpu_count()):
    threads.append(Thread(target=receive_numbers))

for process in processes:
    process.start()
for thread in threads:
    thread.start()

for process in processes:
    process.join()
for thread in threads:
    thread.join()

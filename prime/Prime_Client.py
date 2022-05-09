#!/usr/bin/env python3
from multiprocessing import process, cpu_count
import socket
from math import sqrt
from threading import Thread

server="192.168.1.30"
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

t1=Thread(target=receive_numbers)
t2=Thread(target=receive_numbers)
t3=Thread(target=receive_numbers)
t4=Thread(target=receive_numbers)
t5=Thread(target=receive_numbers)
t6=Thread(target=receive_numbers)
t7=Thread(target=receive_numbers)
t8=Thread(target=receive_numbers)
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

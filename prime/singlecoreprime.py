#!/usr/bin/env python3
from math import sqrt
from sys import argv
import time
start_time=time.time()
primes=[1,2]
try:
        num=int(argv[1])
except IndexError:
    print("Must type an integer value after command")
    exit()
def isPrime(num):
    for i in range(3,num,2):
        for j in range(3,int(sqrt(i))+1,2):
            if i%j==0:
                break
        else:
            primes.append(i)
isPrime(num)
stop_time=time.time()
print (primes)
print("--- %s seconds ---" % (stop_time-start_time))

#!/usr/bin/env python3

from math import sqrt
from sys import argv
import time
from multiprocessing import Pool
from multiprocessing import cpu_count

start_time=time.time()

try:
    num=int(argv[1])
except IndexError:
    print("Must type an integer value after command")
    exit() 

def isPrime(num):
    for i in range(2,num):
        for j in range(2,int(sqrt(i))+1):
            if i%j==0:
                break 
        else:
            print (i," ")


if __name__=='__main__':
    pool=Pool(int(cpu_count()))
    pool.map(isPrime,num)


print("--- %s seconds ---" % (time.time()-start_time))

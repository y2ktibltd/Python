#!/usr/bin/env python3
def fib(n):
    table=[0 for i in range(n+2)]
    table[1]=1
    for i in range(n):
        table[i+1]+=table[i]
        table[i+2]+=table[i]
    return table[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))

#!/usr/bin/env python3
def fib(seq):
    if seq<=1:
        return seq
    else:
        return fib(seq-1)+fib(seq-2)

print(fib(7))


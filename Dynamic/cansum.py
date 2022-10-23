#!/usr/bin/env python3
def cansum(summ,num):
    if summ==0:return True
    if summ<0:return False
    for i in num:
        rem=summ-i
        if cansum(rem,num)==True:
            return True
    return False

print(cansum(7,[2,3]))
print(cansum(7,[5,3,4,7]))
print(cansum(7,[2,4]))
print(cansum(8,[2,3,5]))
#print(cansum(300,[7,14]))

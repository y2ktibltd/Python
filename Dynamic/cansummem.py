#!/usr/bin/env python3
def cansum(s,n,m):
    if s in m:
        return m[s]
    if s==0:
        return True
    if s<0:
        return False
    for i in n:
        if cansum(s-i,n,m)==True:
            m[s]=True
            return True
    m[s]=False
    return False

print(cansum(7,[2,3],{}))
print(cansum(7,[5,3,4,7],{}))
print(cansum(7,[2,4],{}))
print(cansum(8,[2,3,5],{}))
print(cansum(300,[7,14],{}))

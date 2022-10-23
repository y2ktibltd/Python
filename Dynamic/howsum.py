#!/usr/bin/env python3
def howsum(s,n):
    if s==0: return []
    elif s<0:return None
    for i in n:
        r=s-i
        rr = howsum(r,n)
        if rr!=None:
            rr.append(i)
            return rr
    return None


print(howsum(7,[2,3]))
print(howsum(7,[5,3,4,7]))
print(howsum(7,[2,4]))
print(howsum(8,[2,3,5]))
#print(howsum(300,[7,14]))

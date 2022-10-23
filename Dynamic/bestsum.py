#!/usr/bin/env python3
def bestsum(s,n):
    if s==0: return []
    elif s<0:return None
    res=None
    for i in n:
        r=s-i
        rc=bestsum(r,n)
        if rc!=None:
            c=rc.copy()
            c.append(i)
            if res==None:
                res=c.copy()
                continue
            if len(c)<len(res):
                res=c.copy()
    return res



print(bestsum(7,[5,3,4,7]))
print(bestsum(8,[2,3,5]))
print(bestsum(8,[1,4,5]))
#print(bestsum(100,[1,2,5,25]))

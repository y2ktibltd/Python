#!/usr/bin/env python3
def howsum(s,n):
    res=[None for i in range(s+1)]
    res[0]=[]
    for i in range(s):
        if res[i]!=None:
            for j in n:
                if i+j<=s:
                    res[i+j]=res[i].copy()
                    res[i+j].append(j)
    return res[s]

print(howsum(7,[2,3]))
print(howsum(7,[5,3,4,7]))
print(howsum(7,[2,4]))
print(howsum(8,[2,3,5]))
print(howsum(300,[7,14]))


#!/usr/bin/env python3
def cansum(s,n):
    res=[False for i in range(s+1)]
    res[0]=True
    for i in range(s):
        if res[i]==True:
            for j in n:
                if i+j<len(res):
                    res[i+j]=res[i]
    return res[s]

print(cansum(7,[2,3]))
print(cansum(7,[5,3,4,7]))
print(cansum(7,[2,4]))
print(cansum(8,[2,3,5]))
print(cansum(300,[7,14]))


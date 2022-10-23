#!/usr/bin/env python3
def Grid_traveler(gridx,gridy,mem={}):
    key=str(gridx)+","+str(gridy)
    if key in mem: return mem[key]
    if gridx==1 and gridy==1:
        mem[key]=1
        return 1
    if gridx==0 or gridy==0:
        mem[key]=0
        return 0
    mem[key]=Grid_traveler(gridx-1,gridy,mem) + Grid_traveler(gridx,gridy-1,mem)
    print(mem)
    return mem[key]

print(Grid_traveler(1,1))
print(Grid_traveler(2,3))
print(Grid_traveler(3,2))
print(Grid_traveler(3,3))
print(Grid_traveler(18,18))

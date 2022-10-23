#!/usr/bin/env python3
def Grid_traveler(gridx,gridy):
    if gridx==1 and gridy==1:
        return 1
    if gridx==0 or gridy==0:
        return 0
    return Grid_traveler(gridx-1,gridy) + Grid_traveler(gridx,gridy-1)

print(Grid_traveler(1,1))
print(Grid_traveler(2,3))
print(Grid_traveler(3,2))
print(Grid_traveler(3,3))
#print(Grid_traveler(18,18))

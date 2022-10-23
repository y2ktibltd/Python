#!/usr/bin/env python3
def Grid_traveler(x,y):
    grid=[[0 for i in range(x+2)] for j in range(y+2)]
    grid[1][1]=1
    for yy in range(y+1):
        for xx in range(x+1):
            grid[yy][xx+1]+=grid[yy][xx]
            grid[yy+1][xx]+=grid[yy][xx]
    return grid[y][x]

print(Grid_traveler(1,1))
print(Grid_traveler(2,3))
print(Grid_traveler(3,2))
print(Grid_traveler(3,3))
print(Grid_traveler(18,18))


#!/usr/bin/env python3
from random import randint
def sum_of_intervals(nums):
    res=set([])
    for i in nums:
        res.update(range(i[0],i[1]))
    return len(set(res))
    




print(sum_of_intervals([])) # 4
print(sum_of_intervals([(1, 5)])) # 4
print(sum_of_intervals([(1, 5),(1,5)])) # 4
print(sum_of_intervals([(1, 5), (6, 10)])) # 8
print(sum_of_intervals([(1, 5), (1, 5)])) # 4
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)])) # 7
#print(sum_of_intervals([(1,10),(-100_000_001,100_000_000)])) # 2_000_000_000
#print(sum_of_intervals([(-1_000_000_000, 1_000_000_000)])) # 2_000_000_000
#print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)])) # 100_000_030
#print(sum_of_intervals([[randint(randint(-1_000_000_000,0),1),randint(1,randint(1,1_000_000_000))] for i in range(randint(1,10))]))

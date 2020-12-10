list = []
with open('inputs/day1','r') as f:
    for line in f:
        list.append(int(line))

for item in list:
    try:
        ind = list.index((2020-item))
    except:
        ind = None

    if ind is not None:
        print(list[ind]*item)
        break

list = []
with open('inputs/day1','r') as f:
    for line in f:
        list.append(int(line))


'''
FIRST WAY - manual combinations
'''
# - sum all the pairs
#    - put the sums in another list (if less than 2020?)
#    - reuse first answer

# how to get all combinations of a list?
sums = []
for i, a in enumerate(list):
    for j, b in enumerate(list[(i+1):]):
        sums.append(((a+b),(i, j+i+1)))

# - how many pairs are there? ~40k
import numpy as np
n = len(list)
r = 2
print((np.math.factorial(n)) / (np.math.factorial(n-r)*np.math.factorial(r)))

for (sum,(i,j)) in sums:
    for k, item in enumerate(list):
        if sum + item == 2020:
            print(list[i] * list[j] * list[k])


'''
SECOND WAY: n^3 loop
'''
for i in list:
    for j in list:
        for k in list:
            if i + j + k == 2020 and len(set(i,j,k))==3:
                print(i*j*k)

### Another way
'''
THIRD WAY: itertools
'''
from itertools import combinations
from math import prod

for combination in combinations(list):
    if sum(combination) == 2020:
        print(prod(combination))
        break

from collections import defaultdict

ls = []
with open('inputs/day10','r') as f:
    for line in f:
        ls.append(int(line))

ls.append(0) # the charging port

diffs = defaultdict(int)
ls = sorted(ls)
ls.append(ls[-1] + 3)
for x,y in zip(ls, ls[1:]):
    diffs[y-x] += 1

## Part 1
print(diffs[1] * diffs[3])

## Part 2 
paths = [1] + [0] * (len(ls)-1) 

for i, elem in enumerate(ls):
    for offset in range(i-3, i):
        if elem - ls[offset] <= 3:
            paths[i] += paths[offset]

print(paths[-1])

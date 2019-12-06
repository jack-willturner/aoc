from collections import defaultdict

grid = defaultdict(lambda: ([],[]))

orbits = []
with open('inp6.txt', 'r') as f:
    for line in f:
        orbits.append(line.strip().split(')'))

for parent, child in orbits:
    grid[parent][0].append(child)
    grid[child] = ([], [])

#for k, v in grid.items():
#    for child in v:
#        grid[child].append(k)

print(grid)

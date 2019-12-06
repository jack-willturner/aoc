from collections import defaultdict

## [] -> CHILDREN, [] -> PARENTS
grid = defaultdict(lambda: ([],[]))

orbits = []
with open('inp6.txt', 'r') as f:
    for line in f:
        orbits.append(line.strip().split(')'))

for parent, child in orbits:
    grid[parent][0].append(child)
    _ = grid[child]

def partA():
    converged = False
    old_tot = 0
    while(not converged):
        for k, (v,p) in grid.items():
            for child in v:
                if k not in grid[child][1]:
                    grid[child][1].append(k)
                for par in p:
                    if par not in grid[child][1]:
                        grid[child][1].append(par)

        tot = 0
        for k, (v,p) in grid.items():
            parents = set(p)
            tot += len(parents)

        converged = (tot == old_tot)
        old_tot = tot
        print(tot)

for k, (c,p) in grid.items():
    for child in c:
        grid[child][1].append(k)

fringe  = [grid['YOU']]
visited = []
steps = 0

paths = []


while len(fringe) > 0:
    children, parents = fringe[0]
    if 'SAN' in children:
        break
    else:
        for n in (parents+children):
            if n not in visited:
                fringe.append(grid[n])
        steps += 1
        fringe = fringe[1:]

print(steps)

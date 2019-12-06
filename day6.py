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

class Node():
    def __init__(self, name, kids=[], depth=0):
        self.name = name
        self.kids = kids
        self.depth = depth

    def __repr__(self):
        return self.name

def expand(n, depth, visited):
    kids = []
    children, parents = grid[n]
    for node in (children+parents):
        if node == 'SAN':
            print(depth)
        if node not in visited:
            sub_kids = expand(node,depth+1,(visited+[node]))
            kids.append(Node(node, sub_kids, depth))
    return kids

n = Node('YOU', expand('YOU',-1,[]), depth=-1)

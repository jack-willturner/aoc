from math import sqrt, isclose
from tqdm import tqdm

def distance(a,b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    return isclose((distance(a,c) + distance(c,b)), distance(a,b))

def int_between(a,c,b):
    x1 = min(a,b)
    x2 = max(a,b)

    return x1 <= c <= x2

grid = []
x, y = 0, 0
with open('inp10.txt', 'r') as f:
    for line in f:
        x = 0
        for loc in line.strip('\n'):
            if loc == '#':
                grid.append((x,y))
            x += 1
        y += 1

grid_width, grid_height = x, y

def on_path(a, b):

    min_x, max_x = min(a[0], b[0]), max(a[0], b[0])
    min_y, max_y = min(a[1], b[1]), max(a[1], b[1])

    cands = []
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x, y) in grid:
                cands.append((x,y))

    can_shoot = []
    for c in cands:
        if c != a and is_between(a, c, b):
            can_shoot.append(c)

    return can_shoot

def closest(a, ls):
    if len(ls) == 0:
        return None

    distances = [distance(a, l) for l in ls]
    return ls[distances.index(min(distances))]

def partA():

    points_to = {}
    for k in tqdm(grid):
        icansee = 0
        for kk in grid:
            if kk != k:
                if len(on_path(k, kk)) == 0:
                    icansee += 1

        points_to[k] = icansee

    max_ = max(list(points_to.values()))

    print(max_)

    for k, v in points_to.items():
        if v == max_:
            print(k)

    # 344
    # (30, 34)

def partB():
    #starter = (30, 34)
    # do a lap of the grid
    #pointer = (30, 0)

    starter = (11, 13)
    pointer = (11, 0)

    upper, lower = [(x,0) for x in range(grid_width+1)], [(x, grid_height) for x in range(grid_width)]
    right, left  = [(grid_width, y) for y in range(grid_height)], [(0, y) for y in range(grid_height)]
    boundaries   = upper + right + lower + left

    i = boundaries.index(pointer)
    zapped = []
    while len(zapped) < 5:

        on =  on_path(starter, boundaries[i])
        remove_me = closest(starter, on) if len(on) > 0 else None

        if remove_me is not None and (len(remove_me) > 0):
            grid.remove(remove_me)
            zapped.append(remove_me)

        if i == len(boundaries)-1:
            i = 0
        else:
            i += 1

    print(zapped)
    #print(x, y)

#partA()
partB()

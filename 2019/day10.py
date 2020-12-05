from math import sqrt, isclose
from tqdm import tqdm
import numpy as np
from queue import Queue
from collections import defaultdict

def distance(a,b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def angle(a,b,c):
    negate = True if b[0] < c[0] else False

    ## SUBTRACT CENTER POINT
    a = a - c
    b = b - c

    ## NORMALISE VECTOR LENGTHS TO 1
    a = 1./(np.linalg.norm(a)) * a
    b = 1./(np.linalg.norm(b)) * b

    angle = int(np.arccos(np.dot(a,b)) * 1000)
    angle = -angle if negate else angle
    return angle

def is_between(a,c,b):
    return isclose((distance(a,c) + distance(c,b)), distance(a,b))

def int_between(a,c,b):
    x1 = min(a,b)
    x2 = max(a,b)

    return x1 <= c <= x2

def get_grid():
    grid = []
    x, y = 0, 0
    with open('inputs/10', 'r') as f:
        for line in f:
            x = 0
            for loc in line.strip('\n'):
                if loc == '#':
                    grid.append(np.array([x,y]))
                x += 1
            y += 1

    grid_width, grid_height = x, y

    return grid

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

def shoot(grid, p):
    grid_ = []
    for elem in grid:
        if p[0] != elem[0] or p[1] != elem[1]:
            grid_.append(elem)

    return grid_

def partB():
    grid = get_grid()
    # startline
    p_ = np.array([30,0])
    c  = np.array([30,34])


    grid = shoot(grid, c)

    angles = defaultdict(lambda: [])
    for k in grid:
        angles[angle(p_, k,c)].append(k)

    # now sort all the angles by distance
    for k,v in angles.items():
        angles[k] = sorted(v, key=lambda x: distance(c, x))


    n_steps = 201
    sorted_angles = sorted(angles.keys(), key=lambda x: x if x>=0 else x+10000) # there must be a better way to do this
    ap = 0 # angle pointer
    n  = 1
    while(n < n_steps):
        a = sorted_angles[ap]
        try:
            shootme = angles[a][0]
            print(n, ' : ', shootme)
            angles[a].remove(shootme)
            grid = shoot(grid, shootme)
            ap = ap+1 if ap+1 < len(sorted_angles) else 0
        except:
            ap = ap+1 if ap+1 < len(sorted_angles) else 0
        n += 1





partB()

#print(angle(np.array([3,4]), np.array([3,3]), np.array([2,3])))

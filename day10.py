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

grid = {}
x, y = 0, 0
with open('inp10.txt', 'r') as f:
    for line in f:
        x = 0
        for loc in line.strip('\n'):
            if loc == '#':
                grid[(x,y)] = loc
            x += 1
        y += 1

grid_width, grid_height = x, y

def potential(a, b):
    min_x, max_x = min(a[0], b[0]), max(a[0], b[0])
    min_y, max_y = min(a[1], b[1]), max(a[1], b[1])

    cands = []
    #print(list(range(a_x, b_x)))
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            #print(x,y)
            if (x, y) in list(grid.keys()):
                cands.append((x,y))

    can_shoot = []
    for c in cands:
        if is_between(a, c, b):
            can_shoot.append(c)

    return can_shoot

def partA():

    points_to = {}
    for k, v in grid.items():
        print(points_to.values())
        # for all the things that aren't me
        icansee = 0
        for kk, vv in grid.items():
            if kk != k:
                #visible = True
                #for kkk, vvv in grid.items():
                #    if kkk != k and kkk != kk and int_between(k[0],kkk[0],kk[0]) and int_between(k[1],kkk[1],kk[1]):
                #        if is_between(k, kkk, kk):
                #            visible = False

                #if visible:
                #    icansee += 1
                if len(potential(k, kk)) == 0:
                    icansee += 1

            points_to[k] = icansee

    max_ = max(list(points_to.values()))

    for k, v in points_to.items():
        if v == max_:
            print(k)

    # 344
    # (30, 34)

def partB():
    starter = (30, 34)

    # do a lap of the grid
    pointer = (30, 0)

    def potential(a, b):
        min_x = min(a[0], b[0])
        max_x = max(a[0], b[0])

        min_y = min(a[1], b[1])
        max_y = max(a[1], b[1])

        cands = []
        #print(list(range(a_x, b_x)))
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                print(x,y)
                if (x,y) in list(grid.keys()):
                    cands.append((x,y))

        can_shoot = []
        for c in cands:
            if is_between(a, c, b):
                can_shoot.append(c)

        return can_shoot

    def do_lap(x, y):
        while (x <= grid_width):
            x += 1
            print(potential(starter, (x,y)))

        while(y <= grid_height):
            y += 1

        while(x > 0):
            x -= 1

        while(y > 0):
            y -= 1

        while(x < pointer):
            x += 1

    do_lap(pointer[0], pointer[1])

partA()

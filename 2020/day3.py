import numpy as np
## create a 2D array

class Map():
    def __init__(self, fname):
        list = []
        with open('inputs/day3','r') as f:
            for line in f:
                list.append([l for l in line if l != '\n'])

        self.map = np.array(list)
        (self.x, self.y) = self.map.shape

        self.posX = 0
        self.posY = 0
        self.bottom_reached = False

    def move(self, xstep, ystep):

        if (self.posX+xstep) <= self.x:
            self.posX = self.posX + xstep
            self.posY = (self.posY + ystep) % self.y
        else:
            self.bottom_reached = True

        sq = None
        try:
            sq = self.map[self.posX, self.posY]
        except:
            sq = '.'

        return  sq

m = Map('inputs/day3')

tree_counts = []
slopes =[(1,1), (1,3), (1,5), (1,7), (2,1)]

for (xstep, ystep) in slopes:
    cur_tree_count = 0
    m = Map('inputs/day3')

    while(not m.bottom_reached):
        cur_square = m.move(xstep,ystep)
        if cur_square == '#':
            cur_tree_count += 1

    tree_counts.append(cur_tree_count)

print(tree_counts)

print(np.prod(tree_counts))

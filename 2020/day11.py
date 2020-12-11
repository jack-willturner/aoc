inp = []
with open('inputs/day11','r') as f:
    for line in f:
        inp.append((line.replace('\n','')))

from collections import namedtuple
Coord = namedtuple('Coord', 'x y')

## starting grid
grid = {}
x = y = 0
for line in inp:
    x = 0
    for sq in line:
        grid[Coord(x,y)] = sq
        x += 1
    y += 1

def update(grid):
    newgrid = {}

    for coord in grid.keys():
        neighbours =  [(coord.x+1, coord.y+1), (coord.x+1, coord.y), (coord.x+1, coord.y-1),\
                         (coord.x,   coord.y+1), (coord.x, coord.y-1), \
                         (coord.x-1, coord.y+1), (coord.x-1, coord.y), (coord.x-1, coord.y-1)]
        
        # if everything around is empty, we take the seat
        all_empty = all([grid.get(coord, 'L')!='#' for coord in neighbours])
        if grid[coord] == 'L' and all_empty:
            newgrid[coord] = '#'

        # if the seat is occupied, check neighbours
        elif grid[coord] == '#' and sum([1 if grid.get(coord,'.')=='#' else 0 for coord in neighbours]) >= 4:
            newgrid[coord] = 'L'

        # otherwise the state stays the same
        else:
            newgrid[coord] = grid[coord]

    return newgrid

fixpoint = False
history = [list(grid.values())]

nsteps = 0
while(not fixpoint):
    grid = update(grid)
    if list(grid.values()) in history:
        fixpoint = True
    history.append(list(grid.values()))
    nsteps += 1

## PART 1
print(sum([1 if grid.get(coord,'.')=='#' else 0 for coord in grid.keys()]))

## PART 2
import numpy as np

def print_grid(grid):
    width  = max([c.x for c in grid.keys()]) + 1
    height = max([c.y for c in grid.keys()]) + 1
    
    floorplan = np.empty((height, width), dtype=np.string_)

    for (x,y) in grid.keys():
        floorplan[y,x] = grid[Coord(x,y)]

    #print(floorplan)
    for line in floorplan:
        stri = ''
        for char in line:
            stri = stri + char.decode('UTF-8')
        print(stri)

#print_grid(grid)


## PART 2
def update(grid):
    newgrid = {}

    for coord in grid.keys():

        if grid[coord] == '.':
            newgrid[coord] = '.'
        else:

            ### steps
            directions =  [(1, 1), (1, 0), (1, -1),\
                            (0,1), (0, -1), \
                            (-1, 1), (-1, 0), (-1, -1)]
            
            ## for each of the eight directions, scan until you hit something
            neighbours = {}
            for (xstep, ystep) in directions:
                ray_traced = False
                base_coord = coord
                while(not ray_traced and not(grid.get(base_coord,'?')=='?')):
                    lookahead = Coord(base_coord.x+xstep, base_coord.y+ystep)
                    lookahead_state = grid.get(lookahead, '?')
                    
                    if not lookahead_state in ['.','?']:
                        neighbours[lookahead] = lookahead_state
                        ray_traced = True
                    
                    base_coord = lookahead
                    
            # if everything around is empty, we take the seat
            all_empty = all([state in ['L','?'] for state in neighbours.values()])
            if grid[coord] == 'L' and all_empty:
                newgrid[coord] = '#'

            # if the seat is occupied, check neighbours
            elif sum([1 if state=='#' else 0 for state in neighbours.values()]) >= 5:
                newgrid[coord] = 'L'

            # otherwise the state stays the same
            else:
                newgrid[coord] = grid[coord]

    return newgrid


fixpoint = False
history = [list(grid.values())]

nsteps = 0

while(not fixpoint):
    grid = update(grid)
    if list(grid.values()) in history:
        fixpoint = True
    history.append(list(grid.values()))
    nsteps += 1

## PART 2
print(sum([1 if grid.get(coord,'?')=='#' else 0 for coord in grid.keys()]))

from enum import Enum
from intcode import IntcodeComputer

class direction(Enum):
    UP    = 0
    DOWN  = 1
    LEFT  = 2
    RIGHT = 3

def print_grid(grid):
    xs = [x for (x,y) in grid.keys()]
    ys = [y for (x,y) in grid.keys()]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    gridstr = ''
    for y in range(min_y, max_y+1):
        linestr = ''
        for x in range(min_x, max_x+1):
            try:
                bw = grid[x,y]
                if bw == 1:
                    char = '█ '
                else:
                    char = '  '
                linestr = linestr + char
            except:
                linestr = linestr + '  '

        gridstr = gridstr + (linestr + '\n')

    print(gridstr)


class Robot():
    move = {
        direction.UP    : lambda c : (c[0],c[1]+1),
        direction.DOWN  : lambda c : (c[0],c[1]-1),
        direction.LEFT  : lambda c : (c[0]-1,c[1]),
        direction.RIGHT : lambda c : (c[0]+1,c[1]),
    }

    def __init__(self, prog):
        self.p    = direction.UP # pointing
        self.loc  = (0,0)
        self.grid = {}

        self.grid[self.loc] = 1

        self.brain   = IntcodeComputer([], prog)
        self.painted = []

        self.paint()

    def rotate(self, by):
        if self.p == direction.UP:
            self.p = direction.LEFT if by == 0 else direction.RIGHT
        elif self.p == direction.DOWN:
            self.p = direction.RIGHT if by == 0 else direction.LEFT
        elif self.p == direction.RIGHT:
            self.p = direction.UP if by == 0 else direction.DOWN
        elif self.p == direction.LEFT:
            self.p = direction.DOWN if by == 0 else direction.UP

    def paint(self):
        while(True):
            try:
                col = self.grid[self.loc]
            except:
                col = 0
                self.grid[self.loc] = col

            self.brain.outputs  = []
            self.brain.input = [col]*100000
            self.brain.execute()

            if len(self.brain.outputs) > 0:
                paint, turn = self.brain.outputs[0], self.brain.outputs[1]
                #print(paint, turn)
                self.grid[self.loc] = paint
                self.painted.append(self.loc)
                self.rotate(turn)
                self.loc = self.move[self.p](self.loc)
            else:
                break

prog = [3,8,1005,8,328,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,28,1006,0,13,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,54,1,1103,9,10,1006,0,97,2,1003,0,10,1,105,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,91,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,113,2,109,5,10,1006,0,96,1,2,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,146,2,103,2,10,1006,0,69,2,9,8,10,1006,0,25,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,182,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,203,2,5,9,10,1006,0,0,2,6,2,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,236,2,4,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,263,2,105,9,10,1,103,15,10,1,4,4,10,2,109,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,301,1006,0,63,2,105,6,10,101,1,9,9,1007,9,1018,10,1005,10,15,99,109,650,104,0,104,1,21102,387508441116,1,1,21102,1,345,0,1106,0,449,21102,1,387353256852,1,21102,1,356,0,1105,1,449,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,179410308315,0,1,21102,1,403,0,1106,0,449,21101,206199495827,0,1,21102,414,1,0,1105,1,449,3,10,104,0,104,0,3,10,104,0,104,0,21102,718086758760,1,1,21102,1,437,0,1105,1,449,21101,838429573908,0,1,21102,448,1,0,1106,0,449,99,109,2,21202,-1,1,1,21102,1,40,2,21102,480,1,3,21101,470,0,0,1105,1,513,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,475,476,491,4,0,1001,475,1,475,108,4,475,10,1006,10,507,1102,0,1,475,109,-2,2106,0,0,0,109,4,2101,0,-1,512,1207,-3,0,10,1006,10,530,21101,0,0,-3,21202,-3,1,1,21201,-2,0,2,21102,1,1,3,21102,549,1,0,1105,1,554,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,577,2207,-4,-2,10,1006,10,577,22102,1,-4,-4,1106,0,645,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,596,0,0,1106,0,554,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,615,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,637,21201,-1,0,1,21101,637,0,0,106,0,512,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

wall_e = Robot(prog)

unique_visits = set(wall_e.painted)
print(len(unique_visits))

print_grid(wall_e.grid)

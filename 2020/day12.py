from collections import namedtuple
from enum import Enum

Instr = namedtuple('Instr', 'direction distance')
Coord = namedtuple('Coord', 'x y')

ls = []
with open('inputs/day12','r') as f:
    for line in f:
        direction, distance = line[0], int(line[1:].replace('\n',''))
        ls.append(Instr(direction, distance))

class Direction(Enum):
    N = 0
    E = 90
    S = 180
    W = 270

class Ferry:
    def __init__(self, loc, facing, waypoint=None):
        self.loc = loc

        self.waypoint_not_me = False
        if waypoint == None:
            self.waypoint = self.loc
        
        else:
            self.waypoint = waypoint
            self.waypoint_not_me = True
        
        self.facing = facing

    def move(self, instr):
        if instr.direction == 'N':
            self.waypoint = Coord(self.waypoint.x, self.waypoint.y+instr.distance)

        elif instr.direction == 'S':
            self.waypoint = Coord(self.waypoint.x, self.waypoint.y-instr.distance)

        elif instr.direction == 'E':
            self.waypoint = Coord(self.waypoint.x+instr.distance, self.waypoint.y)

        elif instr.direction == 'W':
            self.waypoint = Coord(self.waypoint.x-instr.distance, self.waypoint.y)

        elif instr.direction == 'L':
            if self.waypoint_not_me:
                ### move the waypoint
                if instr.distance == 90:
                    self.waypoint = Coord(-self.waypoint.y, self.waypoint.x)
                elif instr.distance == 180:
                    self.waypoint = Coord(-self.waypoint.x, -self.waypoint.y)
                elif instr.distance == 270:
                    self.waypoint = Coord(self.waypoint.y, -self.waypoint.x) 
            else:
                ### move me
                self.facing = Direction((self.facing.value - instr.distance) % 360)

        elif instr.direction == 'R':
            if self.waypoint_not_me:
                ### move the waypoint
                if instr.distance == 90:
                    self.waypoint = Coord(self.waypoint.y, -self.waypoint.x)
                elif instr.distance == 180:
                    self.waypoint = Coord(-self.waypoint.x, -self.waypoint.y)
                elif instr.distance == 270:
                    self.waypoint = Coord(-self.waypoint.y, self.waypoint.x)
            else:
                ### move me
                self.facing = Direction((self.facing.value + instr.distance) % 360)

        elif instr.direction == 'F':
            if self.waypoint_not_me:
                xstep, ystep = self.waypoint.x, self.waypoint.y
                self.loc = Coord(self.loc.x + instr.distance*xstep, self.loc.y + instr.distance*ystep)
            else:
                self.move(Instr(str(self.facing)[-1], instr.distance))

        return self.loc

### PART 1
ferry = Ferry(Coord(0,0), Direction(90))

for instr in ls:
    ferry.move(instr)
print(abs(ferry.waypoint.x) + abs(ferry.waypoint.y))

### PART 2
ferry = Ferry(Coord(0,0), Direction(90), waypoint=Coord(10,1))

for instr in ls:
    ferry.move(instr)

print(abs(ferry.loc.x) + abs(ferry.loc.y))
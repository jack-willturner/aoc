from itertools import combinations
from numpy import lcm
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

class Moon:
    def __init__(self, position=[0,0,0], name=''):
        self.name = name
        self.position = position
        self.velocity = [0,0,0]

        # period tracking
        self.steps      = 0
        self.periods    = [0,0,0]

    def step(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

        self.steps += 1

    def potential(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def kinetic(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

    def total(self):
        return self.potential() * self.kinetic()

    def __repr__(self):
        return self.name

def partA():
    moons = [Moon([14,15,-2],'Io'),Moon([17,-3,4],'Europa'),Moon([6,12,-13],'Ganymede'),Moon([-2,10,-8],'Callisto')]

    pairs = list(combinations(moons, 2))

    axs  = []
    xs = []
    ys = []
    zs = []

    for j in range(10001):
        tot = 0
        for m in moons:
            tot += m.total()

        ## apply gravity
        for (m1, m2) in pairs:
            for i, (p1, p2) in enumerate(zip(m1.position, m2.position)):
                if p1 < p2:
                    m1.velocity[i] = m1.velocity[i] + 1
                    m2.velocity[i] = m2.velocity[i] - 1
                elif p1 > p2:
                    m1.velocity[i] = m1.velocity[i] - 1
                    m2.velocity[i] = m2.velocity[i] + 1

        for m in moons:
            m.step()

        axs.append(j)
        xs.append(moons[2].position[0])
        ys.append(moons[2].position[1])
        zs.append(moons[2].position[2])

    fig, ax = plt.subplots()
    ax.plot(axs, xs)
    plt.show()

    print('tot: ', tot)

def partB():

    def periods_set(x, y, z):
        return (x > 0) and (y > 0) and (z > 0)

    moons = [Moon([14,15,-2],'Io'),Moon([17,-3,4],'Europa'),Moon([6,12,-13],'Ganymede'),Moon([-2,10,-8],'Callisto')]
    #moons = [Moon([-8,-10,0],'Io'),Moon([5,5,10],'Europa'),Moon([2,-7,3],'Ganymede'),Moon([9,-8,-3],'Callisto')]
    pairs = list(combinations(moons, 2))

    x_visited = []
    y_visited = []
    z_visited = []

    x_steps = 0
    y_steps = 0
    z_steps = 0

    while not (periods_set(x_steps, y_steps, z_steps)):
        ## apply gravity
        for (m1, m2) in pairs:
            for i, (p1, p2) in enumerate(zip(m1.position, m2.position)):
                if p1 < p2:
                    m1.velocity[i] = m1.velocity[i] + 1
                    m2.velocity[i] = m2.velocity[i] - 1
                elif p1 > p2:
                    m1.velocity[i] = m1.velocity[i] - 1
                    m2.velocity[i] = m2.velocity[i] + 1

        xpos_vel = []
        ypos_vel = []
        zpos_vel = []

        for m in moons:
            m.step()
            xpos_vel.append([m.position[0], m.velocity[0]])
            ypos_vel.append([m.position[1], m.velocity[1]])
            zpos_vel.append([m.position[2], m.velocity[2]])

        if xpos_vel in x_visited and x_steps == 0:
            print('X STEPS: ',(m.steps - 1))
            x_steps = m.steps - 1

        if ypos_vel in y_visited and y_steps == 0:
            print('Y STEPS: ',(m.steps - 1))
            y_steps = m.steps - 1

        if zpos_vel in z_visited and z_steps == 0:
            print('Z STEPS: ',(m.steps - 1))
            z_steps = m.steps - 1

        x_visited.append(xpos_vel)
        y_visited.append(ypos_vel)
        z_visited.append(zpos_vel)

        if m.steps % 10000 == 0:
            print(m.steps)


    #loopsin = []
    #for m in moons:
    #    print(m.periods)
    #    m_period = lcm.reduce(m.periods)
    #    loopsin.append(m_period)

    #print(loopsin)
    print(lcm.reduce([x_steps, y_steps, z_steps]))

#partA()
partB()

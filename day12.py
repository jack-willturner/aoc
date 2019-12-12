from itertools import combinations

import matplotlib.pyplot as plt

class Moon:
    def __init__(self, position=[0,0,0], name=''):
        self.name = name
        self.position = position
        self.velocity = [0,0,0]

    def step(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def potential(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def kinetic(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

    def total(self):
        return self.potential() * self.kinetic()

    def __repr__(self):
        return self.name

#moons = [Moon([-1,0,2],'Io'),Moon([2,-10,-7],'Europa'),Moon([4,-8,8],'Ganymede'),Moon([3,5,-1],'Callisto')]
moons = [Moon([14,15,-2],'Io'),Moon([17,-3,4],'Europa'),Moon([6,12,-13],'Ganymede'),Moon([-2,10,-8],'Callisto')]

pairs = list(combinations(moons, 2))

## steps
# apply gravity
# apply velocity

xs, ys1, ys2, ys3, ys4 = [], [], [], [], []

for j in range(1000000001):

    #for m in moons:
    #    print('pos = ', m.position, 'vel=', m.velocity)

    tot = 0
    for m in moons:
        tot += m.total()

    #print('tot: ', tot)

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

    xs.append(j)
    ys1.append(moons[0].position[0])
    ys2.append(moons[1].position[0])
    ys3.append(moons[2].position[0])
    ys4.append(moons[3].position[0])

    #print()


fig, ax = plt.subplots()

ax.plot(xs, ys1)
ax.plot(xs, ys2)

plt.show()

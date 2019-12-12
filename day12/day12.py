from collections import namedtuple
import itertools


# Moon = namedtuple('Moon', 'x y z')

class Moon():
    def __init__(self, x, y, z, name=None):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

        self.dx = 0
        self.dy = 0
        self.dz = 0

    def __str__(self):
        return f'{self.name:2}: pos=<x={self.x:3}, y={self.y:3}, z={self.z:3}>, vel=<x={self.dx:3}, y={self.dy:3}, z={self.dz:3}>'

    def __eq__(self, other):
        positions = (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        velocities = (self.dx == other.dx) and (self.dy == other.dy) and (self.dz == other.dz)
        return positions and velocities

    def __add__(self, other):
        self.dx += self.calc_velocity(self.x, other.x)
        self.dy += self.calc_velocity(self.y, other.y)
        self.dz += self.calc_velocity(self.z, other.z)

        return self

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    @staticmethod
    def calc_velocity(a, b):
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0

    def potential_energry(self):
        return sum(abs(item) for item in (self.x, self.y, self.z))

    def kinetic_energry(self):
        return sum(abs(item) for item in (self.dx, self.dy, self.dz))

    def total_energy(self):
        return self.potential_energry() * self.kinetic_energry()


def step(moons):
    for moon1, moon2 in itertools.permutations(moons, 2):
        moon1 += moon2

    for moon in moons:
        moon.move()

    return moons


def main():
    moons = [
        Moon(4, 1, 1),
        Moon(11, -18, -1),
        Moon(-2, -10, -4),
        Moon(-7, -2, 14),
    ]
    # moons = [
    #     Moon(-1, 0, 2, 'Io'),
    #     Moon(2, -10, -7, 'Eu'),
    #     Moon(4, -8, 8, 'Ga'),
    #     Moon(3, 5, -1, 'Ca'),
    # ]

    for _ in range(1000):
        moons = step(moons)

    print(sum(moon.total_energy() for moon in moons))

def main2():
    moons = [
        Moon(-8, -10, 0, 'Io'),
        Moon(5, 5, 10, 'Eu'),
        Moon(2, -7, 3, 'Ga'),
        Moon(9, -8, -3, 'Ca'),
    ]
    initial_state = [
        Moon(-8, -10, 0, 'Io'),
        Moon(5, 5, 10, 'Eu'),
        Moon(2, -7, 3, 'Ga'),
        Moon(9, -8, -3, 'Ca'),
    ]
    # moons = [
    #     Moon(-1, 0, 2, 'Io'),
    #     Moon(2, -10, -7, 'Eu'),
    #     Moon(4, -8, 8, 'Ga'),
    #     Moon(3, 5, -1, 'Ca'),
    # ]
    # initial_state = [
    #     Moon(-1, 0, 2, 'Io'),
    #     Moon(2, -10, -7, 'Eu'),
    #     Moon(4, -8, 8, 'Ga'),
    #     Moon(3, 5, -1, 'Ca'),
    # ]


    # print(list(moon == i_moon for moon, i_moon in zip(moons, initial_state)))
    # print(all(moon == i_moon for moon, i_moon in zip(moons, initial_state)))

    for count in range(1000000):
    # for count in itertools.count(1):
        moons = step(moons)
        if all(moon == i_moon for moon, i_moon in zip(moons, initial_state)):
            break

    print(count)



if __name__ == "__main__":
    main2()

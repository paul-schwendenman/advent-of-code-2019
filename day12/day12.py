from collections import namedtuple
import itertools


# Moon = namedtuple('Moon', 'x y z')

class Moon():
    def __init__(self, x, y, z, name):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

        self.dx = 0
        self.dy = 0
        self.dz = 0

    def __str__(self):
        return f'{self.name:2}: pos=<x={self.x:3}, y={self.y:3}, z={self.z:3}>, vel=<x={self.dx:3}, y={self.dy:3}, z={self.dz:3}>'

    def __add__(self, other):
        print(self.dx, self.dy, self.dz)
        self.dx += self.calc_velocity(self.x, other.x)
        self.dy += self.calc_velocity(self.y, other.y)
        self.dz += self.calc_velocity(self.z, other.z)
        print(self.dx, self.dy, self.dz)

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
        print(moon1, moon2)
        moon1 += moon2
        print(moon1, moon2)
        print('---------------')

    for moon in moons:
        moon.move()

    return moons


def main():
    # moons = [
    #     Moon(4, 1, 1),
    #     Moon(11, -18, -1),
    #     Moon(-2, -10, -4),
    #     Moon(-7, -2, 14),
    # ]
    moons = [
        Moon(-1, 0, 2, 'Io'),
        Moon(2, -10, -7, 'Eu'),
        Moon(4, -8, 8, 'Ga'),
        Moon(3, 5, -1, 'Ca'),
    ]

    print("step0")
    [print(moon) for moon in moons]
    for _ in range(10):
        moons = step(moons)
    [print(moon) for moon in moons]
    [print(moon.potential_energry()) for moon in moons]
    [print(moon.kinetic_energry()) for moon in moons]
    [print(moon.total_energy()) for moon in moons]


if __name__ == "__main__":
    main()

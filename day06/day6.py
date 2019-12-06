from collections import defaultdict


def create_map(orbits):
    orbit_map = defaultdict(list)

    for orbit in orbits:
        parent, child = orbit.strip().split(')')
        orbit_map[parent].append(child)

    return orbit_map


def count_orbits(orbit_map, key="COM", depth=0):
    # print(f'key: {key} map: {orbit_map}')
    if key in orbit_map:
        total = sum([count_orbits(orbit_map, child, depth+1) for child in orbit_map[key]])
        print(f'key {key} total {total}')
        # print(f'key: {key} direct: {direct} indirect: {indirect}')
        # return direct + indirect
        return total + depth
    else:
        print(f'stop - key {key}, {depth}')
        return depth


def calc_orbits(input):
    return count_orbits(create_map(input))


def main():
    with open('day06/input') as input:
        orbits = calc_orbits(input.readlines())

    return orbits


if __name__ == "__main__":
    print(main())

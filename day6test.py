def find_common(orbits, start='YOU', target='SAN'):
    common_node = None
    seen_by_start = [start]

    current_node = start
    while orbits.get(current_node, None) is not None:
        seen_by_start += [orbits[current_node]]
        current_node = orbits[current_node]

    current_node = target
    while orbits.get(current_node, None) is not None:
        if orbits[current_node] in seen_by_start:
            common_node = orbits[current_node]
            break
        current_node = orbits[current_node]

    return common_node


def count_path(orbits, orbiting, target):
    if orbiting == target:
        return 0
    return 1 + count_path(orbits, orbits[orbiting], target)


def checksum(orbits):
    sum = 0
    for orbiting in orbits.keys():
        sum += count_path(orbits, orbiting, 'COM')
    return sum


def transfers_required(orbits):
    common_node = find_common(orbits)
    return count_path(orbits, 'YOU', common_node) - 1 + count_path(orbits, 'SAN', common_node) - 1


def parse(line):
    orbited, orbiting = line.split(')')
    return (orbiting, orbited)


def main():
    f = open('inp6.txt', 'r')
    orbit_input = list(map(lambda line: line.rstrip(), filter(
        lambda line: len(line) > 0, f.readlines())))
    f.close()

    orbits = {}
    for (orbiting, orbited) in list(map(lambda orbit: parse(orbit), orbit_input)):
        orbits[orbiting] = orbited

    print(f'{checksum(orbits)} orbits total.')
    print(f'common node is {find_common(orbits)}')
    print(
        f'transfers required from YOU -> SAN is {transfers_required(orbits)}')


if __name__ == "__main__":
    main()

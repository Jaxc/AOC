
import re
from collections import Counter
from copy import deepcopy

example_input=[
"""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
]

example_input=[
"""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
]

def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def update_costmap(costmap, currspace):
    has_updated = False

    incamount = 1

    nextspace = []

    dir = costmap[currspace[0]][currspace[1]][1]

    if dir == 'N' or dir == 'S':
        directions = ['W', 'E', dir]

    elif dir == 'W' or dir == 'E':
        directions = ['N', 'S', dir]

for dir in directions:
    if

    if costmap[nextspace[0]][nextspace[1]] is not None:

        if costmap[nextspace[0]][nextspace[1]][1] != dir:
            incamount += 1000

        if costmap[currspace[0]][currspace[1]] is not None:
            if costmap[nextspace[0]][nextspace[1]][0] + incamount < costmap[currspace[0]][currspace[1]][0]:
                costmap[currspace[0]][currspace[1]] = [costmap[nextspace[0]][nextspace[1]][0] + incamount, dir]
                has_updated = True
        else:
            costmap[currspace[0]][currspace[1]] = [costmap[nextspace[0]][nextspace[1]][0] + incamount, dir]
            has_updated = True

    return has_updated
def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    row_separated = example_input[0].split('\n')



    map = []
    for row in row_separated:
        map.append([char for char in row])


    open_spaces = []
    costmap = [[None]*len(map[0]) for _ in map]

    for i in range(len(map)):
        if 'S' in map[i]:
            startpos = [i, map[i].index('S')]
            open_spaces.append([i, map[i].index('S'), True])
        if 'E' in map[i]:
            endpos = [i, map[i].index('E')]
            open_spaces.append([i, map[i].index('E'), False])
        for j in range(len(map[i])):
            if '.' == map[i][j]:
                open_spaces.append([i, j, False])
    # Part 1
    answer = 0

    costmap[startpos[0]][startpos[1]] = [0, 'E']

    continue_looping = True

    while continue_looping:
        continue_looping = False
        for space in open_spaces:
            if space[2] is True:
                continue_looping = continue_looping or update_costmap(costmap, space)

    answer = costmap[endpos[0]][endpos[1]][0]

    print(answer)

    # Part 2
    answer = 0

    print(answer)


    pass

if __name__ == '__main__':
    main()
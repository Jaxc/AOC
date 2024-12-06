
import re
from collections import Counter
from copy import deepcopy

example_input=[
"""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def find_guard_start(map):

    for line in map:
        for char in line:
            if char == '^':
                x = line.index('^')
                y = map.index(line)
    return [x,y]

def try_solution(current_pos, map):
    current_dir='UP'
    #steplog = len(map)*len(map[0])*[[[1,2],'3']]
    stepindex = len(map)*len(map[0])

    while True:
        map[current_pos[1]][current_pos[0]] = 'X'
        if current_dir == 'UP':
            if current_pos[1] == 0:
                #finished
                return None
            if map[current_pos[1] - 1][current_pos[0]] == '#':
                current_dir = 'RIGHT'
            else:
                #steplog[stepindex] = ([current_pos.copy(),current_dir])
                stepindex -= 1
                current_pos[1] = current_pos[1] - 1

        elif current_dir == 'DOWN':
            if current_pos[1] == len(map) - 1:
                # finished
                return None
            if map[current_pos[1] + 1][current_pos[0]] == '#':
                current_dir = 'LEFT'
            else:
                #steplog[stepindex] = ([current_pos.copy(), current_dir])
                stepindex -= 1
                current_pos[1] = current_pos[1] + 1

        elif current_dir == 'LEFT':
            if current_pos[0] == 0:
                # finished
                return None
            if map[current_pos[1]][current_pos[0] - 1] == '#':
                current_dir = 'UP'
            else:
                #steplog[stepindex] = ([current_pos.copy(), current_dir])
                stepindex -= 1
                current_pos[0] = current_pos[0] - 1

        elif current_dir == 'RIGHT':
            if current_pos[0] == len(map[0]) - 1:
                # finished
                return None
            if map[current_pos[1]][current_pos[0] + 1] == '#':
                current_dir = 'DOWN'
            else:
                #steplog[stepindex] = ([current_pos.copy(), current_dir])
                stepindex -= 1
                current_pos[0] = current_pos[0] + 1

        if stepindex == 0:
            return True
        """for item in steplog[:stepindex]:
            if steplog.count(item) > 1 and item != [[1, 2], '3']:
                #we have a loop
                return True"""
    return False

"""def part2(map):
    map_adds = map.copy()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '#':
                # first wall found
                first_wall_pos = [i,j]
                # it can be part of a loop from 4 sides
                if i == 0:
                    or i == len(map) - 1 or j == 0
                for

    return map_adds
def check_loops(map, i, j):
    if map[i][j] == '#':
        # first wall found
        first_wall_pos = [i, j]
        # it can be part of a loop from 4 sides

        if i > 0 and j > 1:
            pot_loop1 = False
            for k in range(j):
                if map[i - 1][k] == '#':
                    second_wall_pos = [i - 1, k]
                    pot_loop1 = True
                    break
            pot_loop2 = False
            for k in range(len(map)-i):
                if map[i + k][j - 1]:
                    third_wall_pos = [i - 1, k]
                    pot_loop2 = True
                    break

            if pot_loop1 and pot_loop2:
                # check that paths are uninterrupted, if they are interrupted they will be caught by other test
                if map[]
"""

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')

    map = []
    for row in row_separated:
        map.append(list(row))

    # Part 1
    answer = 0
    current_pos = find_guard_start(row_separated)
    current_dir = 'UP'

    while True:
        map[current_pos[1]][current_pos[0]] = 'X'
        if current_dir == 'UP':
            if current_pos[1] == 0:
                #finished
                break
            if map[current_pos[1] - 1][current_pos[0]] == '#':
                current_dir = 'RIGHT'
            else:
                current_pos[1] = current_pos[1] - 1

        elif current_dir == 'DOWN':
            if current_pos[1] == len(map) - 1:
                # finished
                break
            if map[current_pos[1] + 1][current_pos[0]] == '#':
                current_dir = 'LEFT'
            else:
                current_pos[1] = current_pos[1] + 1

        elif current_dir == 'LEFT':
            if current_pos[0] == 0:
                # finished
                break
            if map[current_pos[1]][current_pos[0] - 1] == '#':
                current_dir = 'UP'
            else:
                current_pos[0] = current_pos[0] - 1

        elif current_dir == 'RIGHT':
            if current_pos[0] == len(map[0]) - 1:
                # finished
                break
            if map[current_pos[1]][current_pos[0] + 1] == '#':
                current_dir = 'DOWN'
            else:
                current_pos[0] = current_pos[0] + 1

    for row in map:
        answer += row.count('X')

    print(answer)

    # Part 2
    answer = 0

    map = []
    for row in row_separated:
        map.append(list(row))
    final_map = map.copy()

    start_pos = find_guard_start(row_separated)

    for i in range(len(map)):
        print(f"{i}/{len(map)} rows calculated")
        for j in range(len(map[0])):
            #print(f"{j}/{len(map)} rows calculated")
            test_map = deepcopy(map)
            if test_map[i][j] == '#':
                continue
            else:
                test_map[i][j] = '#'
            test = try_solution(deepcopy(start_pos), test_map)
            if test is True:
                answer += 1

    #final_map[start_pos[1]][start_pos[0]] = '^'


    print(answer)


    pass

if __name__ == '__main__':
    main()

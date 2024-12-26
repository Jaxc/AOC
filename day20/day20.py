
import re
from collections import Counter
from copy import deepcopy

example_input=[
"""###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
]



def find_path(map, startpos):
    final_path = []
    active_paths = []
    active_paths.append(startpos)
    for k in range(0, 10000):
        startlen = len(active_paths)
        for path in deepcopy(active_paths):
            if path[0] > 0:
                if map[path[0] - 1][path[1]] == '.':
                    active_paths.append([path[0] - 1, path[1]])
                elif map[path[0] - 1][path[1]] == 'E':
                    map[path[0]][path[1]] = k
                    final_path.append(path)
                    final_path.append([path[0] - 1,path[1]])
                    return final_path, k + 1
            if path[0] < (len(map) - 1):
                if map[path[0] + 1][path[1]] == '.':
                    active_paths.append([path[0] + 1, path[1]])
                elif map[path[0] + 1][path[1]] == 'E':
                    final_path.append(path)
                    final_path.append([path[0] + 1,path[1]])
                    map[path[0]][path[1]] = k
                    return final_path, k + 1
            if path[1] > 0:
                if map[path[0]][path[1] - 1] == '.':
                    active_paths.append([path[0], path[1] - 1])
                elif map[path[0]][path[1] - 1] == 'E':
                    map[path[0]][path[1]] = k
                    final_path.append(path)
                    final_path.append([path[0],path[1] - 1])
                    return final_path, k + 1
            if path[1] < (len(map[0]) - 1):
                if map[path[0]][path[1] + 1] == '.':
                    active_paths.append([path[0], path[1] + 1])
                elif map[path[0]][path[1] + 1] == 'E':
                    map[path[0]][path[1]] = k
                    final_path.append(path)
                    final_path.append([path[0], path[1] + 1])
                    return final_path, k + 1
            map[path[0]][path[1]] = k

        for i in range(startlen):
            final_path.append(active_paths[0])
            active_paths.pop(0)

dirs = [[0,1], [0,-1], [1,0], [-1,0]]

def calc_manhattan(a,b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))
def try_cheat(cord, map, steps):

    possible_target_locations = []
    for i in range(max(1, cord[0] - steps), min(len(map), cord[0] + steps + 1)):
        for j in range(max(1, cord[1] - steps), min(len(map), cord[1] + steps + 1)):
            check_cord = [i, j]
            if calc_manhattan(check_cord,cord) <= steps:
                possible_target_locations.append(check_cord)


    cheats = []
    for poss_cord in possible_target_locations:
        if poss_cord[0] < 1 or poss_cord[0] >= len(map[0]) - 1 or poss_cord[1] < 1 or poss_cord[1] >= len(map) - 1:
            continue

        if map[poss_cord[0]][poss_cord[1]] != '#':
            if map[poss_cord[0]][poss_cord[1]] > map[cord[0]][cord[1]]:
                cheats.append(map[poss_cord[0]][poss_cord[1]] - map[cord[0]][cord[1]] - calc_manhattan(poss_cord,cord))


    return cheats




def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')

    map = []
    for row in row_separated:
        map.append([char for char in row])

    open_spaces = []
    costmap = [[None] * len(map[0]) for _ in map]

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


    path, end_val =  find_path(map, startpos)

    map[endpos[0]][endpos[1]] = end_val

    cheat_list = []
    for i in range(end_val - 2):
        for cheat in try_cheat(path[i], map,2):
            if cheat > 0:
                cheat_list.append(cheat)

    unique_cheats = set(cheat_list)

    # Part 1
    answer = 0

    for cheat in sorted(unique_cheats):
        #print(f" - There are {cheat_list.count(cheat)} cheats that save {cheat} picoseconds.")
        if cheat >= 100:
            answer += cheat_list.count(cheat)


    print(answer)

    # Part 2
    answer = 0

    cheat_list = []

    for i in range(end_val - 2):
        for cheat in try_cheat(path[i], map, 20):
            if cheat > 0:
                cheat_list.append(cheat)

    unique_cheats = set(cheat_list)

    # Part 1
    answer = 0

    for cheat in sorted(unique_cheats):
        print(f" - There are {cheat_list.count(cheat)} cheats that save {cheat} picoseconds.")
        if cheat >= 100:
            answer += cheat_list.count(cheat)

    print(answer)



if __name__ == '__main__':
    main()
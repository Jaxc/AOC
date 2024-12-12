
import re
from collections import Counter

example_input=[
"""AAAA
BBCD
BBCC
EEEC"""
]

example_input=[
"""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
]

example_input=[
"""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
]

def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines


def find_area(map, starx, starty):
    current_sym = map[starx][starty]
    active_paths = [[starx, starty]]
    map[starx][starty] = '.'
    final_paths = []
    while True:
        for path in active_paths.copy():
            if path[0] > 0:
                if map[path[0] - 1][path[1]] == current_sym:
                    if [path[0] - 1, path[1]] not in final_paths:
                        map[path[0] - 1][path[1]] = '.'
                        active_paths.append([path[0] - 1, path[1]])
            if path[0] < (len(map) - 1):
                if map[path[0] + 1][path[1]] == current_sym:
                    if [path[0] + 1, path[1]] not in final_paths:
                        map[path[0] + 1][path[1]] = '.'
                        active_paths.append([path[0] + 1, path[1]])
            if path[1] > 0:
                if map[path[0]][path[1] - 1] == current_sym:
                    if [path[0], path[1] - 1] not in final_paths:
                        map[path[0]][path[1] - 1] = '.'
                        active_paths.append([path[0], path[1] - 1])
            if path[1] < (len(map[0]) - 1):
                if map[path[0]][path[1] + 1] == current_sym:
                    if [path[0], path[1] + 1] not in final_paths:
                        map[path[0]][path[1] + 1] = '.'
                        active_paths.append([path[0], path[1] + 1])
            final_paths.append(active_paths[0])
            active_paths.pop(0)
        if len(active_paths) == 0:
            break

    return [current_sym, None, final_paths]

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')

    map = []
    for row in row_separated:
        map.append([char for char in row])

    fence_map = [[None]*(len(map[0]) + 1) for _ in range(len(map)+2)]
    for row in map:
        for col in row:
            pass

    #areas is [size, borders, [cords]]
    areas = []

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != ".":
                # new region found!
                areas.append(find_area(map,i,j))

    # Part 1
    answer = 0

    # somehow calculate fences
    for area in areas:
        n_fence = 0
        for cord in area[2]:
            if [cord[0] - 1, cord[1]] not in area[2]:
                n_fence += 1
            if [cord[0] + 1, cord[1]] not in area[2]:
                n_fence += 1
            if [cord[0], cord[1] - 1] not in area[2]:
                n_fence += 1
            if [cord[0], cord[1] + 1] not in area[2]:
                n_fence += 1
        answer += n_fence*len(area[2])








    print(answer)

    # Part 2
    answer = 0

    for area in areas:
        perimiter = set()
        n_fence = 0
        for cord in area[2]:
            if [cord[0] - 1, cord[1]] not in area[2]:
                perimiter.add([[cord[0] - 1, cord[1]], [-1, 0]])
            if [cord[0] + 1, cord[1]] not in area[2]:
                perimiter.add([[cord[0] + 1, cord[1]], [+1, 0]])
            if [cord[0], cord[1] - 1] not in area[2]:
                perimiter.add([[cord[0], cord[1] - 1], [0, -1]])
            if [cord[0], cord[1] + 1] not in area[2]:
                perimiter.add([[cord[0], cord[1] + 1], [0, +1]])

        sides = 0



        answer += n_fence * len(area[2])

    print(answer)


    pass

if __name__ == '__main__':
    main()
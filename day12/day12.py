
import re
from collections import Counter

example_input1=[
"""AAAA
BBCD
BBCC
EEEC"""
]

example_input2=[
"""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
]

example_input3=[
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

example_input4=[
"""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
]

example_input5=[
"""AAAEAAAAAA
FFAEAADAAA
FFAAAADACA
FFAABAAAAB
FFABBBABBB
FAAAABBBBB
FAGGABBBBB
FAGAABBBBB"""
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
    #row_separated = example_input5[0].split('\n')

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

    perimiters = []
    for area in areas:
        perimiter = []
        n_fence = 0
        for cord in area[2]:
            if [cord[0] - 1, cord[1]] not in area[2]:
                perimiter.append([[cord[0], cord[1]], ['up']])
            if [cord[0] + 1, cord[1]] not in area[2]:
                perimiter.append([[cord[0], cord[1]], ['down']])
            if [cord[0], cord[1] - 1] not in area[2]:
                perimiter.append([[cord[0], cord[1]], ['left']])
            if [cord[0], cord[1] + 1] not in area[2]:
                perimiter.append([[cord[0], cord[1]], ['right']])

        perimiters.append([area[0], len(area[2]), perimiter])

    #resort perimiters to avoid bug
    for perimiter in perimiters:
        perimiter[2].sort()

    for perimiter in perimiters:
        perimeter_peices = 0
        for i in range(len(perimiter[2])):
            for j in range(i + 1,len(perimiter[2])):
                if perimiter[2][i][1] == ['up'] and perimiter[2][j][1] == ['up']:
                    if perimiter[2][j][0][0] == perimiter[2][i][0][0] and (perimiter[2][j][0][1] + 1 == perimiter[2][i][0][1] or perimiter[2][j][0][1] - 1 == perimiter[2][i][0][1]):
                        perimiter[2][i] = None
                        break
                elif perimiter[2][i][1] == ['down'] and perimiter[2][j][1] == ['down']:
                    if perimiter[2][j][0][0] == perimiter[2][i][0][0] and (perimiter[2][j][0][1] + 1 == perimiter[2][i][0][1] or perimiter[2][j][0][1] - 1 == perimiter[2][i][0][1]):
                        perimiter[2][i] = None
                        break
                elif perimiter[2][i][1] == ['left'] and perimiter[2][j][1] == ['left']:
                    if perimiter[2][j][0][1] == perimiter[2][i][0][1] and (perimiter[2][j][0][0] + 1 == perimiter[2][i][0][0] or perimiter[2][j][0][0] - 1 == perimiter[2][i][0][0]):
                        perimiter[2][i] = None
                        break
                elif perimiter[2][i][1] == ['right'] and perimiter[2][j][1] == ['right']:
                    if perimiter[2][j][0][1] == perimiter[2][i][0][1] and (perimiter[2][j][0][0] + 1 == perimiter[2][i][0][0] or perimiter[2][j][0][0] - 1 == perimiter[2][i][0][0]):
                        perimiter[2][i] = None
                        break
                else:
                    perimeter_peices += 1

                    pass
        pass

        fence_cnt = 0
        for fence in perimiter[2]:
            if fence is not None:
                fence_cnt += 1

        answer += fence_cnt * perimiter[1]

    print(answer)


    pass

if __name__ == '__main__':
    main()
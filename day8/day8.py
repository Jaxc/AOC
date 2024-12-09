
import re
from collections import Counter
from copy import deepcopy

example_input=[
"""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():
    row_separated = read_file()
    #row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')

    map = []
    for row in row_separated:
        map.append(list(row))

    out_map = deepcopy(map)

    # Part 1
    answer = 0

    antenna_pos = {}

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != '.':
                # add to my index
                if map[i][j] not in antenna_pos.keys():
                    antenna_pos[map[i][j]] = []
                antenna_pos[map[i][j]].append([i,j])

    for key in antenna_pos.keys():
        for i in range(len(antenna_pos[key])):
            for j in range(i + 1, len(antenna_pos[key])):
                # calculate antenna antinodes in pairs
                dy = antenna_pos[key][j][0] - antenna_pos[key][i][0]
                dx = antenna_pos[key][j][1] - antenna_pos[key][i][1]

                node1 = [antenna_pos[key][i][0] - dy, (antenna_pos[key][i][1] - dx)]
                node2 = [antenna_pos[key][j][0] + dy, (antenna_pos[key][j][1] + dx)]

                if len(map) > node1[0] >= 0 and len(map[0]) > node1[1] >= 0:
                    out_map[node1[0]][node1[1]] = '#'

                if len(map) > node2[0] >= 0 and len(map[0]) > node2[1] >= 0:
                    out_map[node2[0]][node2[1]] = '#'


                pass

    for row in out_map:
        answer += row.count('#')

    print(answer)

    # Part 2
    answer = 0
    out_map = deepcopy(map)

    for key in antenna_pos.keys():
        for i in range(len(antenna_pos[key])):
            for j in range(i + 1, len(antenna_pos[key])):
                # calculate antenna antinodes in pairs
                dy = antenna_pos[key][j][0] - antenna_pos[key][i][0]
                dx = antenna_pos[key][j][1] - antenna_pos[key][i][1]
                node1 = [antenna_pos[key][i][0], antenna_pos[key][i][1]]

                while True:
                    node1 = [node1[0] - dy, (node1[1] - dx)]
                    if len(map) > node1[0] >= 0 and len(map[0]) > node1[1] >= 0:
                        #answer += 1
                        out_map[node1[0]][node1[1]] = '#'
                    else:
                        break

                node2 = [antenna_pos[key][j][0], (antenna_pos[key][j][1])]
                while True:
                    node2 = [node2[0] + dy, (node2[1] + dx)]
                    if len(map) > node2[0] >= 0 and len(map[0]) > node2[1] >= 0:
                        #answer += 1
                        out_map[node2[0]][node2[1]] = '#'
                    else:
                        break


                pass

    for row in out_map:
        answer += row.count('.')

    answer = len(out_map)*len(out_map[0]) - answer

    print(answer)


    pass

if __name__ == '__main__':
    main()
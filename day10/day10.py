
import re
from collections import Counter

example_input=[
"""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
]



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
        map.append([int(char) for char in row])

    # Part 1
    answer = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                # we have a trailstart
                active_paths = []
                active_paths.append([i,j])
                for k in range(1 , 10):
                    for path in active_paths.copy():
                        if path[0] > 0:
                            if map[path[0] - 1][path[1]] == k:
                                active_paths.append([path[0] - 1, path[1]])
                        if path[0] < (len(map) - 1):
                            if map[path[0] + 1][path[1]] == k:
                                active_paths.append([path[0] + 1, path[1]])
                        if path[1] > 0:
                            if map[path[0]][path[1] - 1] == k:
                                active_paths.append([path[0], path[1] - 1])
                        if path[1] < (len(map[0]) - 1):
                            if map[path[0]][path[1] + 1] == k:
                                active_paths.append([path[0], path[1] + 1])
                        active_paths.pop(0)

                    temp_cords = []
                    [temp_cords.append(val) for val in active_paths if val not in temp_cords]
                    active_paths = temp_cords.copy()

                answer += len(active_paths)





    print(answer)

    # Part 2
    answer = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                # we have a trailstart
                active_paths = []
                active_paths.append([i,j])
                for k in range(1 , 10):
                    for path in active_paths.copy():
                        if path[0] > 0:
                            if map[path[0] - 1][path[1]] == k:
                                active_paths.append([path[0] - 1, path[1]])
                        if path[0] < (len(map) - 1):
                            if map[path[0] + 1][path[1]] == k:
                                active_paths.append([path[0] + 1, path[1]])
                        if path[1] > 0:
                            if map[path[0]][path[1] - 1] == k:
                                active_paths.append([path[0], path[1] - 1])
                        if path[1] < (len(map[0]) - 1):
                            if map[path[0]][path[1] + 1] == k:
                                active_paths.append([path[0], path[1] + 1])
                        active_paths.pop(0)

                    #temp_cords = []
                    #[temp_cords.append(val) for val in active_paths if val not in temp_cords]
                    #active_paths = temp_cords.copy()

                answer += len(active_paths)

    print(answer)


    pass

if __name__ == '__main__':
    main()
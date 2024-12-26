
import re
from collections import Counter
from copy import deepcopy

example_input=[
"""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')

    size = 70 + 1

    map = []
    for i in range(size):
        map.append(['.']*size)

    i = 0
    for cord in row_separated:
        if i > 1024 - 1:
            break
        curr_cord = cord.split(',')
        map[int(curr_cord[1])][int(curr_cord[0])] = '#'
        print(i)
        i+=1


    # Part 1
    answer = 0

    active_paths = []
    active_paths.append([0,0])
    for k in range(0, 1000):
        startlen = len(active_paths)
        for path in deepcopy(active_paths):
            if path[0] > 0:
                if map[path[0] - 1][path[1]] == '.':
                    active_paths.append([path[0] - 1, path[1]])
            if path[0] < (len(map) - 1):
                if map[path[0] + 1][path[1]] == '.':
                    active_paths.append([path[0] + 1, path[1]])
            if path[1] > 0:
                if map[path[0]][path[1] - 1] == '.':
                    active_paths.append([path[0], path[1] - 1])
            if path[1] < (len(map[0]) - 1):
                if map[path[0]][path[1] + 1] == '.':
                    active_paths.append([path[0], path[1] + 1])

            map[path[0]][path[1]] = k

        if map[size - 1][size - 1] != '.':
            answer = map[size - 1][size - 1]
            break

        for i in range(startlen):
            active_paths.pop(0)

        temp_cords = []
        [temp_cords.append(val) for val in active_paths if val not in temp_cords]
        active_paths = temp_cords.copy()


    print(answer)

    # Part 2
    answer = 0



    for j in range(1024, len(row_separated)):

        map = [['.' for _ in map] for _ in map]

        i = 0
        for cord in row_separated:
            if i > j - 1:
                break
            curr_cord = cord.split(',')
            map[int(curr_cord[1])][int(curr_cord[0])] = '#'

            i += 1
        print(j)
        k = 0
        active_paths = []
        active_paths.append([0, 0])
        while True:
            startlen = len(active_paths)
            for path in deepcopy(active_paths):
                if path[0] > 0:
                    if map[path[0] - 1][path[1]] == '.':
                        active_paths.append([path[0] - 1, path[1]])
                if path[0] < (len(map) - 1):
                    if map[path[0] + 1][path[1]] == '.':
                        active_paths.append([path[0] + 1, path[1]])
                if path[1] > 0:
                    if map[path[0]][path[1] - 1] == '.':
                        active_paths.append([path[0], path[1] - 1])
                if path[1] < (len(map[0]) - 1):
                    if map[path[0]][path[1] + 1] == '.':
                        active_paths.append([path[0], path[1] + 1])

                map[path[0]][path[1]] = k

            if map[size - 1][size - 1] != '.':
                answer = map[size - 1][size - 1]
                break

            for i in range(startlen):
                active_paths.pop(0)

            temp_cords = []
            [temp_cords.append(val) for val in active_paths if val not in temp_cords]
            active_paths = temp_cords.copy()

            k += 1

    print(answer)


    pass

if __name__ == '__main__':
    main()
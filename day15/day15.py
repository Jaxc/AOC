
import re
from collections import Counter

example_input=[
"""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
]

example_input2=[
"""##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
]

example_input3=[
"""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""
]

def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def try_move(direction, map, curr_pos):
    if direction == '^':
        mov = [-1,0]
    elif direction == '<':
        mov = [0,-1]
    elif direction == '>':
        mov = [0,1]
    elif direction == 'v':
        mov = [1,0]


    if map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] == '.':
        map[curr_pos[0]][curr_pos[1]] = '.'
        map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] = '@'
        return [curr_pos[0] + mov[0], curr_pos[1] + mov[1]]
    elif map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] == '#':
        return curr_pos
    else:
        i = 1
        while True:
            if map[curr_pos[0] + mov[0] * i][curr_pos[1] + mov[1] * i] == 'O':
                i += 1
            elif map[curr_pos[0] + mov[0] * i][curr_pos[1] + mov[1] * i] == '.':
                map[curr_pos[0]][curr_pos[1]] = '.'
                map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] = '@'
                map[curr_pos[0] + mov[0] * i][curr_pos[1] + mov[1] * i] = 'O'
                return [curr_pos[0] + mov[0], curr_pos[1] + mov[1]]
            elif map[curr_pos[0] + mov[0] * i][curr_pos[1] + mov[1] * i] == '#':
                return curr_pos

def try_move2(direction, map, curr_pos):
    if direction == '^':
        mov = [-1,0]
    elif direction == '<':
        mov = [0,-1]
    elif direction == '>':
        mov = [0,1]
    elif direction == 'v':
        mov = [1,0]


    if map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] == '.':
        map[curr_pos[0]][curr_pos[1]] = '.'
        map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] = '@'
        return [curr_pos[0] + mov[0], curr_pos[1] + mov[1]]
    elif map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] == '#':
        return curr_pos
    else:
        i = 1
        affected_cols = [[i, curr_pos[1], None]]
        while True:
            if mov[0] == 0:
                if map[curr_pos[0] + mov[0] * i][curr_pos[1] + mov[1] * i] == '[' or map[curr_pos[0] + mov[0] * i][curr_pos[1] + mov[1] * i] == ']':
                    i += 1
                elif map[curr_pos[0] + mov[0] * i][curr_pos[1] + mov[1] * i] == '.':
                    map[curr_pos[0]][curr_pos[1]] = '.'
                    map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] = '@'
                    if mov[1] == 1:
                        for j in range(2, i + 1):
                            if j % 2 == 0:
                                map[curr_pos[0] + mov[0] * j][curr_pos[1] + mov[1] * j] = '['
                            else:
                                map[curr_pos[0] + mov[0] * j][curr_pos[1] + mov[1] * j] = ']'
                        return [curr_pos[0] + mov[0], curr_pos[1] + mov[1]]
                    else:
                        for j in range(2, i + 1):
                            if j % 2 == 0:
                                map[curr_pos[0] + mov[0] * j][curr_pos[1] + mov[1] * j] = ']'
                            else:
                                map[curr_pos[0] + mov[0] * j][curr_pos[1] + mov[1] * j] = '['
                        return [curr_pos[0] + mov[0], curr_pos[1] + mov[1]]
                elif map[curr_pos[0] + mov[0] * i][curr_pos[1] + mov[1] * i] == '#':
                    return curr_pos
            else:
                allmove_ok = []
                for col in affected_cols.copy():
                    if col[2] == None:
                        if map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == '[' or map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == ']':
                            currently_active = False
                            if map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == '[':

                                for col_exist in affected_cols.copy():
                                    if col[1] + 1 == col_exist[1]:
                                        if col_exist[2] is None:
                                            currently_active = True

                                if not currently_active:
                                    affected_cols.append([i, col[1] + 1, None])

                            elif map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == ']':
                                for col_exist in affected_cols.copy():
                                    if col[1] - 1 == col_exist[1]:
                                        if col_exist[2] is None:
                                            currently_active = True

                                if not currently_active:
                                    affected_cols.append([i, col[1] - 1, None])

                        elif map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == '.':
                            col[2] = i
                            allmove_ok.append(True)


                        elif map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == '#':
                            return curr_pos

                    else:

                        """if map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == '[' or map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == ']':
                            if map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == '[':
                                if col[1] + 1 not in [col_exist[1] for col_exist in affected_cols]:
                                    affected_cols.append([i, col[1] + 1, None])
                            elif map[curr_pos[0] + mov[0] * i][col[1] + mov[1] * i] == ']':
                                if col[1] - 1 not in [col_exist[1] for col_exist in affected_cols]:
                                    affected_cols.append([i, col[1] - 1, None])
                        else:"""
                        allmove_ok.append(True)

                if len(affected_cols) == allmove_ok.count(True):
                    # all boxes can be moved a step down or up
                    for j in range(len(affected_cols)):
                        if affected_cols is None:
                            for k in range(i, affected_cols[j][0], -1):
                                map[curr_pos[0] + mov[0] * k][affected_cols[j][1] + mov[1] * k] = map[curr_pos[0] + mov[0] * (k - 1)][affected_cols[j][1] + mov[1] * k]
                                map[curr_pos[0] + mov[0] * (k - 1)][affected_cols[j][1] + mov[1] * k] = '.'
                        else:
                            for k in range(affected_cols[j][2], affected_cols[j][0], -1):
                                map[curr_pos[0] + mov[0] * k][affected_cols[j][1] + mov[1] * k] = map[curr_pos[0] + mov[0] * (k - 1)][affected_cols[j][1] + mov[1] * k]
                                map[curr_pos[0] + mov[0] * (k - 1)][affected_cols[j][1] + mov[1] * k] = '.'

                    map[curr_pos[0]][curr_pos[1]] = '.'
                    map[curr_pos[0] + mov[0]][curr_pos[1] + mov[1]] = '@'
                    return [curr_pos[0] + mov[0], curr_pos[1] + mov[1]]
                i += 1

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input2[0].split('\n')

    map = []
    moves = []
    read_mode = 'map'
    for row in row_separated:
        if row == '':
            #move start
            read_mode = ('moves')
        if read_mode == 'map':
            map.append([char for char in row])
        elif read_mode == 'moves':
            moves.extend([char for char in row])

    #find robot

    for i in range(len(map)):
        if '@' in map[i]:
            startpos = [i, map[i].index('@')]

    # Part 1
    answer = 0


    current_pos = startpos
    for move in moves:
        current_pos = try_move(move, map, current_pos)

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'O':
                answer += i * 100 + j

    print(answer)

    # Part 2
    answer = 0
    map = []
    read_mode = 'map'
    for row in row_separated:
        if row == '':
            #move start
            read_mode = ('moves')
        if read_mode == 'map':
            cur_row = []
            for char in row:
                if char == '#':
                    cur_row.extend('##')
                elif char == '.':
                    cur_row.extend('..')
                elif char == 'O':
                    cur_row.extend('[]')
                elif char == '@':
                    cur_row.extend('@.')
            map.append(cur_row)
        elif read_mode == 'moves':
            pass
            #moves.extend([char for char in row])

    for i in range(len(map)):
        if '@' in map[i]:
            startpos = [i, map[i].index('@')]

    current_pos = startpos
    i = 0
    temp_map = [''.join([str(item) for item in row]) for row in map]
    for move in moves:

        if i % 100 == 0:
            pass
        current_pos = try_move2(move, map, current_pos)

        i += 1
        pass

    temp_map = [''.join([str(item) for item in row]) for row in map]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '[':
                pass
                answer += i * 100 + j
                pass

    print(answer)


    pass

if __name__ == '__main__':
    main()
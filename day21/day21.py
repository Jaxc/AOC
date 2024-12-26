
import re
from collections import Counter
from copy import deepcopy
from functools import cache
from itertools import permutations, product, chain

example_input=[
"""029A
980A
179A
456A
379A"""
]


num_pad = [[7,8,9],
           [4,5,6],
           [1,2,3],
           [None, 0, 'a']]

num_pad_rev_map = {'0': [3, 1],
                   '1': [2, 0],
                   '2': [2, 1],
                   '3': [2, 2],
                   '4': [1, 0],
                   '5': [1, 1],
                   '6': [1, 2],
                   '7': [0, 0],
                   '8': [0, 1],
                   '9': [0, 2],
                   'A': [3, 2],
                   }

dir_pad = [[None, '^', 'A'],
           ['<', 'v', '>']]

dir_pad_rev_map = {'^': [0, 1],
                   'A': [0, 2],
                   '<': [1, 0],
                   'v': [1, 1],
                   '>': [1, 2]}

def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines


def get_paths(target, origin):
    """if target[1] == origin[1] or target[0] == origin[0]:
        # Only one path possible
        if target[0] == origin[0]:
            # Horizonal path
            if target[1] > origin[1]:
                return [(target[1] - origin[1]) *['>']]
            else:
                return [(origin[1] - target[1]) * ['<']]
        else:
            # Vertical path
            if target[0] > origin[0]:
                return [(target[0] - origin[0]) *['v']]
            else:
                return [(origin[0] - target[0]) * ['^']]
    else:"""
    if target[1] > origin[1]:
        hor_moves = (target[1] - origin[1]) * ['>']
    else:
        hor_moves = (origin[1] - target[1]) * ['<']

    if target[0] > origin[0]:
        ver_moves = (target[0] - origin[0]) * ['v']
    else:
        ver_moves = (origin[0] - target[0]) * ['^']

    path_elements = ver_moves + hor_moves

    permuts = list(permutations(path_elements))

    if origin[0] == 3 and target[1] == 0 or origin[1] == 0 and target[0] == 3:
        pass
        for i in range(len(permuts) - 1, -1, -1):
            if origin[0] == 3:
               if list(permuts[i][0:origin[1]]) == ['<']*origin[1]:
                   permuts.pop(i)
            if origin[1] == 0:
                if list(permuts[i][0: 3 - origin[0]]) == ['v'] * (3 - origin[0]):
                    permuts.pop(i)


    return permuts


def part1(moves):
    current_moves = moves


    for robot in range(2):

        new_code = []
        for code in current_moves:
            current_pos = 'A'
            move_paths = []
            new_map = []
            for move in code:
                option_paths = []
                for option in move:
                    submove_paths = []

                    for submove in option:
                        new_paths = key_pad_path(submove, current_pos)
                        submove_paths.append(new_paths)
                        pass
                        current_pos = submove
                        pass
                    for step1 in product(*submove_paths):
                        option_paths.append(list(chain.from_iterable(step1)))
                move_paths.append(option_paths)

            for step1 in product(*move_paths):
                new_map.append(list(chain.from_iterable(step1)))

            new_code.append([new_map])

        for code in new_code:
            max_len = len(code[0][0])
            for elem in code[0]:
                max_len = min(max_len, len(elem))

            for i in range(len(code[0]) - 1, -1, -1):
                if len(code[0][i]) > max_len:
                    code[0].pop(i)
        if robot != 1:
            current_moves = deepcopy(new_code)

        pass

    ret_value = []
    for code in new_code:
        ret_value.append(len(code[0][0]))
    return ret_value


@cache
def key_pad_path(target, origin):
    if origin == target:
        return ['A']
    if dir_pad_rev_map[target][1] > dir_pad_rev_map[origin][1]:
        hor_moves = (dir_pad_rev_map[target][1] - dir_pad_rev_map[origin][1]) * ['>']
    else:
        hor_moves = (dir_pad_rev_map[origin][1] - dir_pad_rev_map[target][1]) * ['<']

    if dir_pad_rev_map[target][0] > dir_pad_rev_map[origin][0]:
        ver_moves = (dir_pad_rev_map[target][0] - dir_pad_rev_map[origin][0]) * ['v']
    else:
        ver_moves = (dir_pad_rev_map[origin][0] - dir_pad_rev_map[target][0]) * ['^']

    path_elements = ver_moves + hor_moves

    poss_paths = list(permutations(path_elements))

    # remove paths that goes over invalid square
    unique_path = []
    for p in poss_paths:
        p_list = list(p)
        if p_list + ['A'] not in unique_path:
            if dir_pad_rev_map[origin][0] == 0 and p_list[0:dir_pad_rev_map[origin][1]] == ['<']*dir_pad_rev_map[origin][1]:
                pass
            elif dir_pad_rev_map[origin][0] == 1 and dir_pad_rev_map[origin][1] == 0 and p_list[0] == '^':
                pass
            else:
                unique_path.append(p_list + ['A'])



    return unique_path

def main():
    row_separated = read_file()
    #row_separated = example_input[0].split('\n')


    # Part 1
    answer = 0

    current_pos = num_pad_rev_map['A']
    moves=[]
    # Get shortest key combination
    for row in row_separated:
        row_moves = []
        for char in row:
            target = num_pad_rev_map[char]
            paths = get_paths(target, current_pos)
            unique_path = []
            for p in paths:
                if list(p) + ['A'] not in unique_path:

                    unique_path.append(list(p) + ['A'])

            row_moves.append(unique_path)

            current_pos = num_pad_rev_map[char]
            pass
        moves.append(row_moves)

    # iterate through robots pressing the keypads

    min_moves = part1(moves)

    for code, min_move in zip(row_separated, min_moves):
        answer += int(code[0:3]) * min_move

    print(answer)

    # Part 2
    answer = 0

    print(answer)


    pass

if __name__ == '__main__':
    main()
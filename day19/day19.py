
import re
from collections import Counter
from copy import deepcopy
from functools import cache

example_input=[
"""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

@cache
def matchtarget(target):
    total_correct = 0
    for towel in towels:
        if towel == target:
            total_correct += 1
        elif target[:len(towel)] == towel:
            new_matches = matchtarget(target[len(towel):])
            if new_matches > 0:
                total_correct += new_matches
                continue
            else:
                continue

    return total_correct



def main():
    global towels
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')

    tower_State = True
    targets = []
    for row in row_separated:
        if tower_State:
            towels = row.split(', ')
            tower_State = False
        else:
            targets.append(row)
    targets.pop(0)

    # Part 1
    answer = 0

    for target in targets:
        answer += matchtarget(target)

    print(answer)

    # Part 2
    answer = 0



    print(answer)


    pass

if __name__ == '__main__':
    main()
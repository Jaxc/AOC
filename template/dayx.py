
import re
from collections import Counter
from copy import deepcopy

example_input=[
""""""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    row_separated = example_input[0].split('\n')

    map = []
    for row in row_separated:
        map.append([int(char) for char in row])

    # Part 1
    answer = 0

    print(answer)

    # Part 2
    answer = 0

    print(answer)


    pass

if __name__ == '__main__':
    main()
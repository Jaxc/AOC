
import re
from collections import Counter

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
    #row_separated = example_input[0].split('\n')

    # Part 1
    answer = 0

    print(answer)

    # Part 2
    answer = 0

    print(answer)


    pass

if __name__ == '__main__':
    main()

import re
from collections import Counter

example_input=[
"""3   4
4   3
2   5
1   3
3   9
3   3"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')


    left_values = []
    right_values = []
    for row in row_separated:
        values = row.split('   ')
        left_values.append(int(values[0]))
        right_values.append(int(values[1]))

    left_values.sort()
    right_values.sort()

    # Part 1
    answer = 0
    for i in range(len(left_values)):
        answer = answer + abs(left_values[i]-right_values[i])

    print(answer)

    # Part 2
    answer = 0
    right_occurences = Counter(right_values)
    for elem in left_values:
        answer = answer + elem * right_occurences[elem]

    print(answer)


    pass

if __name__ == '__main__':
    main()
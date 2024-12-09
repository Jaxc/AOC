
import re
from collections import Counter

example_input=[
"""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
]

op_list=['+','*']

def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')
    #row_separated = example_input[0].split('\n')

    # Part 1
    answer = 0
    j = 0
    for equation in row_separated:
        print(f"row: {j}/{len(row_separated)}")
        j += 1
        split1 = equation.split(':')
        target = split1[0]
        operators = split1[1].split()
        possibple_ops = pow(3, len(operators)-1)

        possible_answer = [int(operators[0])]

        for i in range(len(operators)-1):
            for current_answer in possible_answer.copy():
                possible_answer.append(current_answer * int(operators[i + 1]))
                possible_answer.append(current_answer + int(operators[i + 1]))
                possible_answer.append(int(str(current_answer) + operators[i + 1]))

        for final_answer in possible_answer[-possibple_ops:]:
            if final_answer == int(target):
                answer = int(answer) + int(final_answer)
                break


    print(answer)

    # Part 2
    answer = 0

    print(answer)


    pass

if __name__ == '__main__':
    main()
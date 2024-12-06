
import re
from collections import Counter

example_input=[
"""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def calc_ok_seq(values, inital_len):
    new_values=[]
    for value in values:
        new_values.append(int(value))
    values = new_values
    valid_asc = True
    valid_dec = True
    first_wrong_asc_value = []
    first_wrong_dec_value = []
    for i in range(len(values) - 1):
        if int(values[i]) == (int(values[i + 1]) + 1) or int(values[i]) == (int(values[i + 1]) + 2) or int(values[i]) == (int(values[i + 1]) + 3):
            valid_asc = False
            first_wrong_asc_value.append(i)
        elif int(values[i]) == (int(values[i + 1]) - 1) or int(values[i]) == (int(values[i + 1]) - 2) or int(values[i]) == (int(values[i + 1]) - 3):
            valid_dec = False
            first_wrong_dec_value.append(i)
        else:
            valid_dec = False
            valid_asc = False
            first_wrong_dec_value.append(i)
            first_wrong_asc_value.append(i)

    if valid_asc or valid_dec:
        return 1
    else:
        if len(values) == inital_len:
            answer = 0
            for i in range(inital_len):
                test_values = values.copy()
                test_values.pop(i)
                answer += calc_ok_seq(test_values, inital_len)
            if answer > 0:
                return 1
        return 0


def main():
    row_separated = read_file()
    #row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')

    # Part 1
    answer = 0

    for row in row_separated:
        values = row.split()
        valid_asc = True
        valid_dec = True
        for i in range(len(values) - 1) :
            if int(values[i]) == (int(values[i + 1]) + 1) or int(values[i]) == (int(values[i + 1]) + 2) or int(values[i]) == (int(values[i + 1]) + 3):
                valid_asc = False
            elif int(values[i]) == (int(values[i + 1]) - 1) or int(values[i]) == (int(values[i + 1]) - 2) or int(values[i]) == (int(values[i + 1]) - 3):
                valid_dec = False
            else:
                valid_dec = False
                valid_asc = False

        if valid_asc or valid_dec:
            answer += 1

        pass

    print(answer)

    # Part 2
    answer = 0
    for row in row_separated:
        answer += calc_ok_seq(row.split(), len(row.split()))

    print(answer)


    pass

if __name__ == '__main__':
    main()
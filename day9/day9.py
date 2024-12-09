
import re
from collections import Counter

example_input=[
"""2333133121414131402"""
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

    # get expanded file table
    expanded_file_table = []
    file_id = 0
    is_data = True
    for char in row_separated[0]:
        if is_data is True:
            expanded_file_table.extend(int(char) * [file_id])
            file_id += 1
            is_data = False
        else:
            expanded_file_table.extend(int(char) * ['.'])
            is_data = True

    #compress file table
    max_legit_value = len(expanded_file_table) - 1
    for i in range(len(expanded_file_table)):
        if expanded_file_table[i] == '.':
            for j in range(max_legit_value, i, -1):
                if expanded_file_table[j] != '.':
                    expanded_file_table[i] = expanded_file_table[j]
                    expanded_file_table[j] = '.'
                    answer += i * expanded_file_table[i]
                    max_legit_value = j
                    break
        else:
            answer += i * expanded_file_table[i]

    # calc answer



    print(answer)

    # Part 2
    answer = 0

    # get expanded file table
    expanded_table = []
    file_id = 0
    is_data = True
    for char in row_separated[0]:
        if is_data is True:
            expanded_table.append([int(char), file_id])
            file_id += 1
            is_data = False
        else:
            expanded_table.append([int(char), '.'])
            is_data = True

    first_empty_space = 0
    for i in range(len(expanded_table) - 1, 0, -1):
        if i % 100:
            print(f"{i} / {len(expanded_table)}")
        if expanded_table[i][1] != '.':
            for j in range(first_empty_space, i):
                if expanded_table[j][1] == '.':
                    if expanded_table[j][0] >= expanded_table[i][0]:
                        expanded_table[j][0] -= expanded_table[i][0]
                        expanded_table.insert(j, expanded_table[i].copy())
                        expanded_table[i + 1][1] = '.'
                        break


    index_cnt = 0
    for elem in expanded_table:
        for cnt in range(elem[0]):
            if elem[1] != '.':
                answer += index_cnt*elem[1]
            index_cnt += 1

    print(answer)


    pass

if __name__ == '__main__':
    main()
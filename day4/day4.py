
import re
from collections import Counter

example_input=[
"""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
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

    #check horizontal
    for row in row_separated:
        for i in range(len(row)-3):
            if row[i:i+4] == "XMAS":
                answer += 1
            elif row[i:i+4] == "SAMX":
                answer += 1

    #check vertical
    for i in range(len(row_separated) - 3):
        for j in range(len(row_separated[0])):
            if ''.join([item[j] for item in row_separated[i:i+4]]) == "XMAS":
                answer += 1
            elif ''.join([item[j] for item in row_separated[i:i+4]]) == "SAMX":
                answer += 1

    # check diagonal
    for i in range(len(row_separated) - 3):
        for j in range(len(row_separated[0])-3):
            current_guess = ''.join([row_separated[i][j], row_separated[i+1][j+1], row_separated[i+2][j+2], row_separated[i+3][j+3]])
            if current_guess == "XMAS":
                answer += 1
            elif current_guess == "SAMX":
                answer += 1
            current_guess = ''.join([row_separated[i+3][j], row_separated[i+2][j+1], row_separated[i+1][j+2], row_separated[i][j+3]])
            if current_guess == "XMAS":
                answer += 1
            elif current_guess == "SAMX":
                answer += 1


    print(answer)

    # Part 2
    answer = 0

    # check diagonal
    for i in range(len(row_separated) - 2):
        for j in range(len(row_separated[0])-2):
            found_1 = False
            found_2 = False
            found_X = True
            current_guess = ''.join([row_separated[i][j], row_separated[i+1][j+1], row_separated[i+2][j+2]])
            if current_guess == "MAS":
                pass
            elif current_guess == "SAM":
                pass
            else:
                found_X = False

            current_guess = ''.join([row_separated[i+2][j], row_separated[i+1][j+1], row_separated[i][j+2]])
            if current_guess == "MAS":
                pass
            elif current_guess == "SAM":
                pass
            else:
                found_X = False

            if found_X == True:
                answer += 1



    print(answer)


    pass

if __name__ == '__main__':
    main()
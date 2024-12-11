
import re
from collections import Counter
from collections import defaultdict

example_input=[
"""0 1 10 99 999"""
]

example_input=[
"""125 17"""
]

n_blinks = 75

def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def add_new_or_add(input, output, key):
    if int(key) in input:
        output[key] = input[key] + 1
    else:
        output.update({int(key): 1})



def do_blink(input):
    output = {}
    for i in input.keys():
        stone_str = str(i)
        if i == 0:
            new_key = 1
            if int(new_key) in output:
                output[new_key] = output[new_key] + input[i]
            else:
                output.update({int(new_key): input[i]})
        elif (len(stone_str) % 2) == 0 :
            # split stone

            new_key = int(stone_str[:int(len(stone_str) / 2)])
            if int(new_key) in output:
                output[new_key] = output[new_key] + input[i]
            else:
                output.update({int(new_key): input[i]})

            new_key = int(stone_str[int(len(stone_str) / 2):])
            if int(new_key) in output:
                output[new_key] = output[new_key] + input[i]
            else:
                output.update({int(new_key): input[i]})
        else:
            new_key = i*2024
            if int(new_key) in output:
                output[new_key] = output[new_key] + input[i]
            else:
                output.update({int(new_key): input[i]})

    return output

def main():
    row_separated = read_file()[0]
    #row_separated = row_separated[0:-1]
    #row_separated = example_input[0]

    map = []
    #for row in row_separated:
    row_separated = [int(char) for char in row_separated.split()]

    # Part 1
    answer = 0

    new_line = {}

    for entry in row_separated:
        if int(entry) in new_line:
            new_line[entry] = new_line[entry] + 1
        else:
            new_line.update({int(entry): 1})



    for i in range(n_blinks):
        print(f"{i} / {n_blinks}")
        new_line = do_blink(new_line)


    for entry in new_line.keys():
        answer += new_line[entry]


    print(answer)

    # Part 2
    answer = 0

    print(answer)


    pass

if __name__ == '__main__':
    main()
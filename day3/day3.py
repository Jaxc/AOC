
import re
from collections import Counter

example_input=[
#"""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)"""
"""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        #lines = f.read()

    return lines

def main():
    row_separated = read_file()
    #row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')
    #row_separated = example_input[0]

    str = ""
    for row in row_separated:
        str = str + row

    row_separated = str

    # Part 1
    answer = 0


    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\))", row_separated)

    for match in matches:
        numbers = re.findall(r"\d+", match)
        answer += int(numbers[0])*int(numbers[1])

    print(answer)

    # Part 2
    #row_separated = read_file()
    #row_separated = example_input
    answer = 0

    str = ""
    debugstr = ""
    debugcnt = 0
    last_valid_index = 0
    currently_do = True
    pruned_string = ""

    for i in range(len(row_separated) - 7):
        if row_separated[i:i + 7] == "don't()":
            if currently_do is True:
                pruned_string = pruned_string + row_separated[last_valid_index:i]
                currently_do = False
                debugstr = debugstr + row_separated[i:i + 7]
            # stop string
        elif row_separated[i:i + 4] == "do()":
            if currently_do == False:
                debugcnt +=1
                currently_do = True
                last_valid_index = i
                debugstr = debugstr + row_separated[i:i + 4]
    if currently_do is True:
        pass
        pruned_string = pruned_string + row_separated[last_valid_index:-1]


    str = str + pruned_string

    print(debugstr)
    print(debugcnt)

    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\))", str)

    for match in matches:
        numbers = re.findall(r"\d+", match)
        answer += int(numbers[0])*int(numbers[1])

    print(answer)


    pass

if __name__ == '__main__':
    main()
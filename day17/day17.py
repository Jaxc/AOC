
import re
from collections import Counter
from copy import deepcopy
from datetime import datetime

example_input=[
"""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
]

example_input2=[
"""Register A: 12345678
Register B: 0
Register C: 0

Program: 2,4,1,0,7,5,1,5,0,3,4,5,5,5,3,0"""
]

def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines


def get_combo_op(ref):
    if int(ref) <= 3:
        return int(ref)
    elif ref == 4:
        return rega
    elif ref == 5:
        return regb
    elif ref == 6:
        return regc



def main():
    calc_start = datetime.now()
    global rega, regb, regc
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input2[0].split('\n')

    rega = 0
    regb = 0
    regc = 0


    for row in row_separated:
        if re.match(r"Register A: (\d+)", row):
            rega = int(re.match(r"Register A: (\d+)", row).group(1))
        elif re.match(r"Register B: (\d+)", row):
            regb = int(re.match(r"Register B: (\d+)", row).group(1))
        elif re.match(r"Register C: (\d+)", row):
            regc = int(re.match(r"Register C: (\d+)", row).group(1))
        elif re.match(r"Program: (\d+)", row):
            program = re.match(r"Program: ((\d+,*)*)", row).group(1)

    program = program.split(',')
    program = [int(entry) for entry in program]
    # Part 1
    answer = 0

    # op adv, bxl, bst, jnz, bxc, out, bdv, cdv

    op_pointer = 0
    output = []

    part1_start = datetime.now()
    while True:
        if op_pointer >= len(program):
            break
        match program[op_pointer]:
            case 0:
                # division
                rega = rega // pow(2, get_combo_op(program[op_pointer + 1]))
                op_pointer += 2

            case 1:
                # XOR
                regb = regb ^ program[op_pointer + 1]
                op_pointer += 2
            case 2:
                regb = get_combo_op(program[op_pointer + 1]) % 8
                op_pointer += 2
            case 3:
                if rega != 0:
                    op_pointer = program[op_pointer + 1]
                else:
                    op_pointer += 2
            case 4:
                regb = regb ^ regc
                op_pointer += 2
            case 5:
                output.append(get_combo_op(program[op_pointer + 1]) % 8)
                op_pointer += 2
            case 6:
                regb = rega // pow(2, get_combo_op(program[op_pointer + 1]))
                op_pointer += 2
            case 7:
                regc = rega // pow(2, get_combo_op(program[op_pointer + 1]))
                op_pointer += 2
        pass


    answer = ','.join([str(i) for i in output])
    print(answer)

    # Part 2
    answer = 0
    op_pointer = 0

    part2_start = datetime.now()
    for row in row_separated:
        if re.match(r"Register B: (\d+)", row):
            regb_init = int(re.match(r"Register B: (\d+)", row).group(1))
        elif re.match(r"Register C: (\d+)", row):
            regc_init = int(re.match(r"Register C: (\d+)", row).group(1))

    next_val = [0]

    for curr_calc in range(len(program)):
        solution = []

        """if (((i % 8) ^ 2) ^ i != 2:
            continue"""

        for next in deepcopy(next_val):

            for i in range(next*pow(2,3), (next + 1)*pow(2,3)):



                rega = i
                regb = regb_init
                regc = regc_init
                output = []
                op_pointer = 0
                j = 0


                while True:
                    if op_pointer >= len(program):
                        break

                    match program[op_pointer]:
                        case 0:
                            # division
                            rega = rega // pow(2, get_combo_op(program[op_pointer + 1]))
                            op_pointer += 2

                        case 1:
                            # XOR
                            regb = regb ^ program[op_pointer + 1]
                            op_pointer += 2
                        case 2:
                            regb = get_combo_op(program[op_pointer + 1]) % 8
                            op_pointer += 2
                        case 3:
                            if rega != 0:
                                op_pointer = program[op_pointer + 1]
                            else:
                                op_pointer += 2
                        case 4:
                            regb = regb ^ regc
                            op_pointer += 2
                        case 5:
                            output_to_be = get_combo_op(program[op_pointer + 1]) % 8
                            output.append(output_to_be)
                            if output_to_be == program[len(program) - 1 - curr_calc + j]:
                                j += 1
                                if j > curr_calc:
                                    solution.append(i)
                                    break
                            else:
                                break


                            op_pointer += 2
                        case 6:
                            regb = rega // pow(2, get_combo_op(program[op_pointer + 1]))
                            op_pointer += 2
                        case 7:
                            regc = rega // pow(2, get_combo_op(program[op_pointer + 1]))
                            op_pointer += 2
                    pass


                #if j > curr_calc:
                    #break
        next_val=[]
        next_val.extend(solution)

    answer = next_val.pop()
    print(answer)

    part2_done= datetime.now()
    pass

    print(f"Total time: {part2_done - calc_start}")
    print(f"Part1 time: {part2_start - part1_start}")
    print(f"Part2 time: {part2_done - part2_start}")


if __name__ == '__main__':
    main()
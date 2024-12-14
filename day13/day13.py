
import re
from collections import Counter
import numpy as np

example_input=[
"""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():
    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')
    exp = r"Button .: X\+(\d+), Y\+(\d+)"
    price_exp = r"Prize: X=(\d+), Y=(\d+)"

    machines = []

    for i in range(0,len(row_separated),4):

        test = re.search(exp, row_separated[i])
        a_btn = [int(test.group(1)), int(test.group(2))]

        test = re.search(exp, row_separated[i+1])
        b_btn = [int(test.group(1)), int(test.group(2))]


        test = re.search(price_exp, row_separated[i+2])
        prize_cords = [int(test.group(1)), int(test.group(2))]

        machines.append([a_btn, b_btn, prize_cords])


    # Part 1
    answer = 0

    solutions1 = 150*[[0,0]]
    j = 0
    for machine in machines:

        solutions = []
        for a in range(int(max(machine[2][0]/machine[0][0], machine[2][1]/machine[0][1])) + 1):
            for b in range(int(max(machine[2][1] / machine[1][1], machine[2][1] / machine[1][1])) + 1):
                if machine[0][0] * a + machine[1][0] * b == machine[2][0] and machine[0][1] * a + machine[1][1] * b == machine[2][1]:
                    # Match!
                    solutions.append([a, b])
                    #solutions1[j] = [a, b]
                    j += 1

        #find cheapest match
        if len(solutions) > 0:
            cheapest = solutions[0][0] * 3 + solutions[0][1]
            for i in range(len(solutions)):
                cheapest = min(cheapest, solutions[i][0] * 3 + solutions[i][1])
            answer += cheapest



    pass

    """while True:
        for current in current_try.copy():
            if cur_x < int(machine[2][0]) and cur_y < int(machine[2][1]):
                if current[0][0] == machine[2][0] and current[0][1] == machine[2][1]:
                    #MATCH
                    solutions.append([current[1], current[1]])
                    current_try.pop(0)
                    break
                elif current[0][0] > machine[2][0] or current[0][1] > machine[2][1]:
                    #solution will never lead anywhere
                    current_try.pop(0)
                    break
                # press a
                new_cord = [current[0][0] + machine[0][0], current[0][1] + machine[0][1]]
                current_try.append([new_cord, current[1] + 1, current[2]])
                # press b
                new_cord = [current[0][0] + machine[1][0], current[0][1] + machine[1][1]]
                current_try.append([new_cord, current[1], current[2] + 1])
                current_try.pop(0)"""



    print(answer)

    # Part 2
    answer = 0

    machines=[]
    for i in range(0,len(row_separated),4):

        test = re.search(exp, row_separated[i])
        a_btn = [int(test.group(1)), int(test.group(2))]

        test = re.search(exp, row_separated[i+1])
        b_btn = [int(test.group(1)), int(test.group(2))]


        test = re.search(price_exp, row_separated[i+2])
        prize_cords = [int(test.group(1)) + 10000000000000, int(test.group(2)) + 10000000000000]

        machines.append([a_btn, b_btn, prize_cords])


    solutions2 = []
    for machine in machines:

        A = np.array([[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]])
        B = np.array([machine[2][0], machine[2][1]])

        matrix_solution = list(np.linalg.solve(A, B))
        matrix_solution = [int(round(temp)) for temp in matrix_solution]

        if machine[0][0] * int(matrix_solution[0]) + machine[1][0] * int(matrix_solution[1]) == machine[2][0] and machine[0][1] * int(matrix_solution[0]) + machine[1][1] * int(matrix_solution[1]) == \
                machine[2][1]:
            # Match!
            solutions2.append(matrix_solution)
            answer += int(matrix_solution[0]) * 3 + int(matrix_solution[1])

    print(answer)


    pass

if __name__ == '__main__':
    main()
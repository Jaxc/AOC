
import re
from collections import Counter

example_input=[
"""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():

    mapsize=[103,101]



    row_separated = read_file()
    row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n')

    map = [['.' for _ in range(mapsize[1])] for _ in range(mapsize[0])]
    robot_stats = []
    for row in row_separated:
        cords = list(re.findall(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)", row)[0])
        robot_stats.append([int(char) for char in cords])
    # Part 1
    answer = 0
    current_step = robot_stats.copy()
    for _ in range(100):
        next_step = []
        for robot in current_step:
            new_pos = [robot[0] + robot[2], robot[1] + robot[3], robot[2], robot[3]]
            if new_pos[0] < 0:
                new_pos[0] += mapsize[1]
            elif new_pos[0] > mapsize[1] - 1:
                new_pos[0] -= mapsize[1]

            if new_pos[1] < 0:
                new_pos[1] += mapsize[0]
            elif new_pos[1] > mapsize[0] - 1:
                new_pos[1] -= mapsize[0]

            next_step.append(new_pos)

        current_step = next_step.copy()

    quadrants = [0,0,0,0]
    for robot in current_step:
        map[robot[1]][robot[0]] = 'R'
        if int(mapsize[1]/2) > robot[0] and int(mapsize[0]/2) > robot[1]:
            quadrants[0] += 1
        elif int(mapsize[1]/2) > robot[0] and int(mapsize[0]/2) < robot[1]:
            quadrants[1] += 1
        elif int(mapsize[1]/2) < robot[0] and int(mapsize[0]/2) > robot[1]:
            quadrants[2] += 1
        elif int(mapsize[1]/2) < robot[0] and int(mapsize[0]/2) < robot[1]:
            quadrants[3] += 1

    answer = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    print(answer)

    # Part 2
    answer = 0

    current_step = robot_stats.copy()
    i = 1
    while True:
        next_step = []
        for robot in current_step:
            new_pos = [robot[0] + robot[2], robot[1] + robot[3], robot[2], robot[3]]
            if new_pos[0] < 0:
                new_pos[0] += mapsize[1]
            elif new_pos[0] > mapsize[1] - 1:
                new_pos[0] -= mapsize[1]

            if new_pos[1] < 0:
                new_pos[1] += mapsize[0]
            elif new_pos[1] > mapsize[0] - 1:
                new_pos[1] -= mapsize[0]

            next_step.append(new_pos)



        robot_pos = [[pos[0], pos[1]] for pos in next_step]
        unique_pos = []
        for j in robot_pos:
            if j not in unique_pos:
                unique_pos.append(j)

        if len(robot_pos) == len(unique_pos):
            answer = i
            break

        current_step = next_step.copy()
        i+=1

    print(answer)


    pass

if __name__ == '__main__':
    main()
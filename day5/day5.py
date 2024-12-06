
import re
from collections import Counter

example_input=[
"""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
]



def read_file():
    with open('input.txt') as f:
        lines = f.read().split('\n\n')

    return lines

def check_row(page, dependency_list):
    for dep in dependency_list:
        current_list = page
        for j in range(len(current_list)):
            if current_list[j] in dep[1]:
                if dep[0] in current_list:
                    if current_list.index(dep[0]) < current_list.index(dep[1]):
                        pass
                    else:
                        return 0

    return int(page[int(len(page)/2)])

def check_and_fix_row(page, dependency_list):
    for dep in dependency_list:
        current_list = page
        for j in range(len(current_list)):
            if current_list[j] in dep[1]:
                if dep[0] in current_list:
                    if current_list.index(dep[0]) < current_list.index(dep[1]):
                        pass
                    else:
                        page.pop(current_list.index(dep[0]))
                        page = page[0:current_list.index(dep[1])] + [dep[0]] + page[current_list.index(dep[1]):]
                        result = check_row(page, dependency_list)
                        if result == 0:
                            return check_and_fix_row(page, dependency_list)
                        else:
                            return result

    return 0
    #return int(page_elem[int(len(page_elem)/2)])

def main():
    row_separated = read_file()
    #row_separated = row_separated[0:-1]
    #row_separated = example_input[0].split('\n\n')

    # Part 1
    answer = 0

    dependency_list = []
    for dependency in row_separated[0].split('\n'):
        dependency_list.append(dependency.split('|'))

    print_pages = row_separated[1].split('\n')
    print_pages.pop(-1)

    for page in print_pages:
        answer += check_row(page.split(','), dependency_list)
    """                for prev_page in range(len(print_pages) - j):
                        if current_list[j + prev_page + 1] in dep[0]:
                            pass"""

    """        for dep in dependency_list:
        if int(dep[1]) == int(page):
            pass"""

    print(answer)

    # Part 2
    answer = 0
    for page in print_pages:
        answer += check_and_fix_row(page.split(','), dependency_list)
    print(answer)


    pass

if __name__ == '__main__':
    main()
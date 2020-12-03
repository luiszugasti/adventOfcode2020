# day 3
from typing import List

from day2.day2 import open_file


# each line is 31 chars long

def navigate_tree_line(line, previous_position):
    zero_indexed_position = previous_position - 1
    zero_indexed_position = zero_indexed_position % len(line)

    print("zero_indexed_position: {}, previous_position: {}".format(zero_indexed_position, previous_position))
    if line[zero_indexed_position] == '#':
        return 1
    return 0


def navigate_trees(lines: List[str], starting_position: int) -> List[int]:
    trees_encountered = [0] * 5
    positions = [starting_position] * 5
    rules = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 1),  # should be 1, 2 but easier to skip every other line
    ]

    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(rules) - 1):
            rule = rules[j]
            trees_encountered[j] = trees_encountered[j] + navigate_tree_line(line, positions[j])
            positions[j] = positions[j] + rule[0]

        if i % 2 == 0:
            trees_encountered[4] = trees_encountered[4] + navigate_tree_line(line, positions[4])
            positions[4] = positions[4] + rules[4][0]

    return trees_encountered


def main():
    puzzle_input = open_file("day3_input.txt")
    answer = navigate_trees(puzzle_input, 1)

    print("values before multiplying: {}, {}, {}, {}, {}".format(answer[0], answer[1], answer[2], answer[3], answer[4]))
    print("answer: {}".format(answer))


if __name__ == '__main__':
    main()

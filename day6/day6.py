# day 6
from typing import List, re

from day2.day2 import open_file
from day4.day4 import is_newline, input_lines_to_dict, count_valid_passports


def input_lines_to_set(lines: str) -> set:
    pass


def count_times_answered_yes(lines: List[str]) -> int:
    running_list = []
    count = 0
    for line in lines:
        if is_newline(line):
            positive_answers = set(running_list)
            count = count + len(positive_answers)
            running_list = []
        else:
            running_list = running_list + (list(line))

    return count


def count_times_all_answered_yes(lines: List[str]) -> int:
    running_set = set()
    count = 0
    is_first_entry = True
    for line in lines:
        if is_newline(line):
            print(len(running_set))
            count = count + len(running_set)
            running_set = set()
            is_first_entry = True
        else:
            temp_answers = set(list(line))  # This is SO lazy.
            if is_first_entry:
                running_set = temp_answers
                is_first_entry = False
            else:
                running_set = running_set.intersection(temp_answers)

    return count


def main():
    puzzle_input = open_file("day6_input.txt")
    answer = count_times_all_answered_yes(puzzle_input)

    print("answer: {}".format(answer))


if __name__ == '__main__':
    main()

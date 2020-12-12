# day 4
from enum import Enum, auto
from typing import List
import re

from day2.day2 import open_file


def verify_height(hgt: str) -> bool:
    unit_of_measure = hgt[-2:]
    count = hgt[:-2]
    if str.isdigit(count):
        count_int = int(count)
        if unit_of_measure == 'in':
            return 59 <= count_int <= 76
        if unit_of_measure == 'cm':
            return 150 <= count_int <= 193
    return False


def verify_hair_color(hcl: str) -> bool:
    hash_char = hcl[0]
    value = hcl[1:]
    p = re.compile('[0-9a-f]')

    if hash_char == '#':
        if len(value) == 6:
            hit = p.findall(value)
            if len(hit) == 6:
                return True
    return False


def verify_eye_color(ecl: str) -> bool:
    valid_colors = ['amb',
                    'blu',
                    'brn',
                    'gry',
                    'grn',
                    'hzl',
                    'oth']
    return ecl in valid_colors


def verify_passport_id(pid: str) -> bool:
    return str.isdigit(pid) and len(pid) == 9
    pass


valid_passport = {
    "BYR": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "IYR": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "EYR": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "HGT": verify_height,
    "HCL": verify_hair_color,
    "ECL": verify_eye_color,
    "PID": verify_passport_id,
}


def is_newline(string: str) -> bool:
    """Don't check for newline character since open_file removes newlines"""
    return len(string) == 0


def is_valid_passport(available_fields):
    """Return true if all fields in ValidPassword are present"""
    for key in valid_passport:
        print(key)
        if key not in available_fields:
            return False

        check = valid_passport[key]
        if not check(available_fields[key]):
            return False

    return True


def passport_lines_to_dict(lines) -> dict:
    """Accept lines from passport batch file and create a dictionary"""
    passport = {}
    for line in lines:
        entries = line.split(" ")
        for entry in entries:
            key_value = entry.split(":")
            passport[key_value[0].upper()] = key_value[1]

    return passport


def count_valid_passports(lines: List[str]):
    running_list = []
    count = 0
    for line in lines:
        if is_newline(line):
            current_passport = passport_lines_to_dict(running_list)
            if is_valid_passport(current_passport):
                count = count + 1
            running_list = []
        else:
            running_list.append(line)
    return count


def main():
    puzzle_input = open_file("day4_input.txt")
    answer = count_valid_passports(puzzle_input)

    print("answer: {}".format(answer))
    # print("answer: {}".format(reduce((lambda x, y: x * y), answer)))


if __name__ == '__main__':
    main()

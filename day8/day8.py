# day8.py
import copy
from typing import Tuple

from day2.day2 import open_file


def parse_input_to_puzzle_scope(puzzle_input):
    parsed_instructions = []
    for entry in puzzle_input:
        parsed_instructions.append(parse_instruction(entry))
    return parsed_instructions


def parse_instruction(input):
    action = input[:3]
    value = int(input[4:])
    return (action, value)


def find_value_accumulator(instructions) -> Tuple[int, bool]:
    seen = [False] * len(instructions)
    accumulator = 0
    program_counter = 0

    def _is_cycle():
        return seen[program_counter]

    while (program_counter < len(instructions)):

        if _is_cycle():
            return accumulator, True

        action, value = instructions[program_counter]
        seen[program_counter] = True
        if action == "acc":
            program_counter = program_counter + 1
        if action == "nop":
            program_counter = program_counter + 1
        if action == "jmp":
            program_counter = program_counter + value

        if action == "acc":
            accumulator = accumulator + value

    return accumulator, False


def fix_the_program(instructions):
    for i in range(len(instructions)):
        action, value = instructions[i]
        if action == "nop" or action == "jmp":
            temp_instructions = copy.deepcopy(instructions)
            if action == "nop":
                temp_instructions[i] = "jmp", instructions[i][1]
            if action == "jmp":
                temp_instructions[i] = "nop", instructions[i][1]

            value, isCycle = find_value_accumulator(temp_instructions)
            if not isCycle:
                return value


if __name__ == '__main__':
    puzzle_input = open_file("day8_input.txt")
    parsed_instructions = parse_input_to_puzzle_scope(puzzle_input)
    answer = find_value_accumulator(parsed_instructions)

    print("answer: {}".format(answer))

    answer = fix_the_program(parsed_instructions)

    print("answer: {}".format(answer))

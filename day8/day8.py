# day8.py
from day2.day2 import open_file


def parse_instruction(input):
    action = input[:3]
    value = int(input[4:])
    return (action, value)


def find_value_accumulator(puzzle_input):
    parsed_instructions = []
    for entry in puzzle_input:
        parsed_instructions.append(parse_instruction(entry))

    seen = [False] * len(parsed_instructions)
    accumulator = 0
    program_counter = 0

    def _is_cycle():
        return seen[program_counter]

    while (True):
        action, value = parsed_instructions[program_counter]
        seen[program_counter] = True
        if action == "acc":
            program_counter = program_counter + 1
        if action == "nop":
            program_counter = program_counter + 1
        if action == "jmp":
            program_counter = program_counter + value

        if _is_cycle():
            return accumulator
        if action == "acc":
            accumulator = accumulator + value


if __name__ == '__main__':
    puzzle_input = open_file("day8_input.txt")
    answer = find_value_accumulator(puzzle_input)

    print("answer: {}".format(answer))

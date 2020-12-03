# day 2
import os


def open_file(file_name: str) -> list:
    with open(os.getcwd() + "/" + file_name, "r", encoding="utf-8") as f:
        entries = f.readlines()
        puzzle_input = [s[0:len(s) - 1] for s in entries]

    return puzzle_input


def process_entry(line: str) -> list:
    """Take a line from day2_input.txt and return important values"""
    split_index = line.index(":")
    split_range_index = line.index("-")
    password = line[split_index + 2:len(line)]

    return [split_index, split_range_index, password]


def is_valid_password_sled_rental(input: str) -> bool:
    """Return true if password is valid, false otherwise"""
    [split_index, split_range_index, password] = process_entry(input)

    rule = {'letter': input[split_index - 1],
            'minimum': int(input[0:split_range_index]),
            'maximum': int(input[split_range_index + 1:split_index - 2])
            }

    letters = {}
    for letter in password:
        if letter in letters:
            letters[letter] = 1 + letters[letter]
        else:
            letters[letter] = 1

    if rule['letter'] not in letters:
        return False

    letter_amt = letters[rule['letter']]

    if rule['minimum'] > letter_amt or rule['maximum'] < letter_amt:
        return False
    else:
        return True


def is_valid_password_toboggan_rental(input: str) -> bool:
    """
    Return true if password is valid, false otherwise
    Important: there is no zero indexing in the rule provided.
    """
    [split_index, split_range_index, password] = process_entry(input)

    rule = {'letter': input[split_index - 1],
            'index': [int(input[0:split_range_index]) - 1,
                      int(input[split_range_index + 1:split_index - 2]) - 1
                      ],
            }

    return (password[rule['index'][0]] == rule['letter']) ^ (password[rule['index'][1]] == rule['letter'])


def main():
    puzzle_input = open_file("day2_input.txt")
    amount_valid = 0
    for entry in puzzle_input:
        if is_valid_password_toboggan_rental(entry):
            amount_valid = amount_valid + 1

    print("{}".format(amount_valid))


if __name__ == '__main__':
    main()

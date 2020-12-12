# day 5
def seat_id(ticket: str) -> int:
    row = 0
    column = 0
    for i in range(len(ticket)):
        if i < 7:
            if ticket[i] == 'B':
                row = 2 ** (6 - i) + row
        else:
            if ticket[i] == 'R':
                column = 2 ** (9 - i) + column

    return row * 8 + column


def main():
    puzzle_input = open_file("day4_input.txt")
    answer = count_valid_passports(puzzle_input)

    print("answer: {}".format(answer))
    # print("answer: {}".format(reduce((lambda x, y: x * y), answer)))


if __name__ == '__main__':
    main()

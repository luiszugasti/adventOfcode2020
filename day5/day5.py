# day 5
from typing import List

from day2.day2 import open_file


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


def find_max_seat_id(tickets: List[str]) -> int:
    ids = [seat_id(ticket) for ticket in tickets]

    return max(ids)


def find_my_seat(tickets: List[str]) -> int:
    ids = [seat_id(ticket) for ticket in tickets]
    list.sort(ids)
    min = ids[0]

    # could also do without some complexity and determine the difference of sums
    # of a list that has my ticket id and one without my id
    for i in range(len(ids)):
        sample = ids[i]
        if i + min != sample:
            return sample - 1


def main():
    puzzle_input = open_file("day5_input.txt")
    answer = find_my_seat(puzzle_input)

    print("answer: {}".format(answer))


if __name__ == '__main__':
    main()

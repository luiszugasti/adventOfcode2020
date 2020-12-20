# day 7
import re
from typing import List, Tuple, Dict, Set

from day2.day2 import open_file
from day6.day6 import count_times_all_answered_yes


def traverse_bags(bags: Dict[str, Dict[str, int]], bags_to_search: Set[str], goal_bag: str):
    hits = set()
    if bags_to_search is None:
        bags_to_search = bags.keys()

    for bag in bags_to_search:
        if str in bags.keys() and True:
            pass


def process_rule(rule: str) -> Tuple[str, Dict[str, int]]:
    """ for each rule, returns a (bag_color, internal_bags) representation."""
    [this_color, *bag_strings] = rule[:-6].split(" bags contain ")
    if bag_strings[0] == "no other":
        return this_color, {}
    bag_strings = re.compile(" bag[s], ").split(bag_strings[0])

    bags = {}
    for bag in bag_strings:
        amount = int(bag[0])
        color = bag[2:]
        bags[color] = amount
    return this_color, bags


def process_all_rules(rules: List[str]) -> Tuple[Dict[str, Dict[str, int]], set]:
    """ returns a dictionary representation of all rules. returns a set of all unique colors."""
    rule_dict = {}
    unique_colors = set()
    for rule in rules:
        color, bag_list = process_rule(rule)
        rule_dict[color] = bag_list
        unique_colors.add(color)
    return rule_dict, unique_colors


def find_all_bag_colors(rules: List[str], bag_color: str) -> int:
    rules, unique_colors = process_all_rules(rules)
    current_colors = set()
    possible_bags = 0

    for bag_color in rules.keys():
        # traverse the dictionary one level deep.
        # if we find our bag, add this to our current_colors set. Include the amount.

        # loop until we have no more bags to search (make sure to not go into cycles - more on this
        # later).

        # return the amount of bags that can fit our gold bag.
        t = 9


if __name__ == '__main__':
    puzzle_input = open_file("day7_input.txt")
    answer = find_all_bag_colors(puzzle_input, "shiny gold")

    print("answer: {}".format(answer))

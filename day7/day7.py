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
    # I couldn't find anything in Python that would be extremely complicated without using lookaheads it seems,
    # so I am employing a simple pipeline of splitting.
    temp_strings = (re.compile(" bag[s]*\.").split(rule))[0]
    temp_strings = re.compile(" bag[s]*, ").split(temp_strings)
    [bag_color, first_bag_string] = re.compile(" bags contain ").split(temp_strings[0])

    bag_strings = [first_bag_string] + temp_strings[1:]

    if bag_strings[0] == "no other":
        return bag_color, {}

    bags = {}
    for bag in bag_strings:
        amount = int(bag[0])
        color = bag[2:]
        bags[color] = amount
    return bag_color, bags


def process_all_rules(rules: List[str]) -> Tuple[Dict[str, Dict[str, int]], set]:
    """ returns a dictionary representation of all rules. returns a set of all unique colors."""
    rule_dict = {}
    unique_colors = set()
    for rule in rules:
        color, bag_list = process_rule(rule)
        rule_dict[color] = bag_list
        unique_colors.add(color)
    return rule_dict, unique_colors


def find_num_internal_bags(rules: List[str], bag_color: str) -> int:
    """ TODO: refactor"""
    rules, unseen_colors = process_all_rules(rules)
    current_colors = set()

    for rule_bag in rules.keys():
        if bag_color in rules[rule_bag].keys():
            current_colors.add(rule_bag)
            unseen_colors.remove(rule_bag)

    while len(current_colors) > 0:
        new_colors = set()
        remove_colors = set()
        for rule_bag in unseen_colors:
            for follow_on_bag in current_colors:
                if follow_on_bag in rules[rule_bag].keys():
                    new_colors.add(rule_bag)
                    remove_colors.add(rule_bag)

        current_colors = new_colors
        for color in remove_colors:
            unseen_colors.remove(color)

    return len(rules) - len(unseen_colors)


def find_all_bag_colors(rules: List[str], bag_color: str) -> int:
    rules, unseen_colors = process_all_rules(rules)
    current_colors = set()

    for rule_bag in rules.keys():
        if bag_color in rules[rule_bag].keys():
            current_colors.add(rule_bag)
            unseen_colors.remove(rule_bag)

    while len(current_colors) > 0:
        new_colors = set()
        remove_colors = set()
        for rule_bag in unseen_colors:
            for follow_on_bag in current_colors:
                if follow_on_bag in rules[rule_bag].keys():
                    new_colors.add(rule_bag)
                    remove_colors.add(rule_bag)

        current_colors = new_colors
        for color in remove_colors:
            unseen_colors.remove(color)

    return len(rules) - len(unseen_colors)


if __name__ == '__main__':
    puzzle_input = open_file("day7_sample_input.txt")
    answer = find_num_internal_bags(puzzle_input, "shiny gold")

    print("answer: {}".format(answer))

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

    # find first (and only) occurrence of shiny gold bag
    # get the bags that it contains, and build a tree
    # once we have the bags it contains, repeat the process.
    # if we get a bag that has no bags inside it, then put no entry inside
    # do until we have no more bags to traverse.

    # Then, in reverse fashion, return amount. For simplicity, traverse the tree we have created.
    # each node will return its current amount * the amount of bags inside it.
    # Leaf case: return only the amount of bags that it contains in the parent level
    # Top level will accumulate. Remember not to add the value for the shiny gold bag.

    # Create the tree of internal bags
    current_pointers = []
    tree = {}
    for entry in rules[bag_color].keys():
        tree[entry] = {}
        tree[entry]["amount"] = rules[bag_color][entry]
        tree[entry]["next"] = {}
        current_pointers.append((entry, tree[entry]))

    while len(current_pointers) > 0:
        new_bags = []
        for bag_color, tree_pointer in current_pointers:
            for entry in rules[bag_color].keys():
                inner = {}
                inner[entry] = {}
                inner[entry]["amount"] = rules[bag_color][entry]
                inner[entry]["next"] = {}
                new_bags.append((entry, inner[entry]))
                tree_pointer["next"] = {**inner, **tree_pointer["next"]}

        current_pointers = new_bags

    # Traverse the tree of internal parts and aggregate the results.
    def _traverse_tree(node) -> int:
        if not node["next"]:
            return node["amount"]
        value = 0
        for bag in node["next"].keys():
            value = value + _traverse_tree(node["next"][bag])
        return value * node["amount"] + node["amount"]

    answer = 0
    for node in tree.keys():
        answer = answer + _traverse_tree(tree[node])
    return answer


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
    puzzle_input = open_file("day7_input.txt")
    answer = find_num_internal_bags(puzzle_input, "shiny gold")

    print("answer: {}".format(answer))

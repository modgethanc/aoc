#!/usr/bin/python3

"""
AOC 2017 Day :
"""

import sys
def main():
    """
    Main entry point.
    """

    inputfile = open(sys.argv[1], 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line.rstrip())
    inputfile.close()

    #print("part one solution: " + str(solve_part_one(inputs)))
    print("part two solution: " + str(solve_part_two(inputs)))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    children = get_all_children(inputs)
    bases = get_all_bases(inputs)

    return list(set(bases).difference(set(children)))[0]

def get_base(line):
    """
    Given a single line from the input, return its base element.
    """

    return line.split(" ")[0]

def get_children(line):
    """
    Given a single line from the input, return a string list of its children.
    This should be empty if it has no children.
    """

    linesplit = line.split(" -> ")
    if len(linesplit) > 1:
        return linesplit[1].split(", ")
    else:
        return []

def get_all_children(inputs):
    """
    Given a full set of inputs, return a string list containing all unique
    children.
    """

    items = []

    for line in inputs:
        items.extend(get_children(line))

    return set(items)

def get_all_bases(inputs):
    """
    Given a full set of inputs, return a string list containing all unique
    bases.
    """

    items = []

    for line in inputs:
        items.append(get_base(line))

    return set(items)

def solve_part_two(inputs):
    """
    Solver for part two.
    """

    solution = 0

    input_tree = make_tree(inputs)
    culprits = find_unbalanced_items(input_tree)
    unbalanced = []
    for culprit in culprits:
        unbalanced.append(find_culprit(tower_weights(culprit, input_tree)))

    print(unbalanced)
    unbalanced.sort(key=lambda item:item[1])

    culprit = unbalanced[0]

    culprit_weight = sum_weights(culprit[0], input_tree)
    print(culprit_weight)
    delta = culprit[1] - culprit_weight
    print(delta)

    solution = input_tree.get(culprit[0]).get("weight") + delta

    return solution

def get_weight(line):
    """
    Given a single line of input, return the weight as an int of the base item.
    """

    # this split is ugly but it works

    return int(line.split("(")[1].split(")")[0])

def make_tree(inputs):
    """
    Given a full set of inputs, return a dict that represents each item in the
    following way:
        "item": {
            "children":["child1", "child2", "child3"],
            "weight": weight
            }
    If the item has no children, its value should be blank.
    """

    tree = {}

    for line in inputs:
        tree.update({get_base(line):{
            "children": get_children(line),
            "weight": get_weight(line)
                }
            })

    return tree

def sum_weights(item, tree):
    """
    Given a single item, return the weight of its entire tower based on the
    given input set.
    """

    total = tree.get(item).get("weight")

    for child in tree.get(item).get("children"):
        total += sum_weights(child, tree)

    return total

def tower_weights(item, tree):
    """
    Given a single item, return a list of tuples of (item, weight) representing
    the total weight of each of its children, sorted by weight.
    """

    weights = []

    for child in tree.get(item).get("children"):
        weights.append((child, sum_weights(child, tree)))

    weights.sort(key=lambda item:item[1])

    return weights

def is_balanced(item, tree):
    """
    Given a single item, return whether or not the values of its children are
    balanced.
    """

    weights = []
    weight_chart = tower_weights(item, tree)

    for sum in weight_chart:
        weights.append(sum[1])

    return len(set(weights)) <= 1

def find_unbalanced_items(tree):
    """
    Given a single tree, return all unbalanced items in it.
    """

    culprits = []

    for item in tree:
        if not is_balanced(item, tree):
            culprits.append(item)

    return culprits

def find_culprit(culprits):
    """
    Given a list of unbalanced tuples (item, weight), return a tuple of
    (culprit, desired weight)
    """

    smallest = culprits[0][1]
    biggest = culprits[-1][1]
    comp = culprits[1][1]

    if smallest == comp:
        # this means the biggest is unique
        return (culprits[-1][0], smallest)
    else:
        return (culprits[0][0], biggest)

if __name__ == '__main__':
    sys.exit(main())

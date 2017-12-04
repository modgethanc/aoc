#!/usr/bin/python3

"""
AOC 2017 Day 4:
    a low-stress little string compare exercise, pecked at gently while running
    lab hours. on an actual keyboard!
"""

import sys

def main():
    """
    Main entry point.
    """

    inputfile = open(sys.argv[1], 'r')
    input = []
    for line in inputfile:
        input.append(line)
    inputfile.close()

    print("part one solution: " + str(solve_part_one(input)))
    print("part two solution: " + str(solve_part_two(input)))

    return 0

def solve_part_one(input):
    """
    Solver for part one.
    """

    solution = 0

    for test in input:
        test = test.rstrip()
        #print("testing: "+test)
        if validate(test):
            solution += 1

    return solution

def validate(passphrase):
    """
    Checks if a single passphrase is valid; returns true if so.
    """

    wordlist = passphrase.split()
    checklist = set(wordlist)

    if len(wordlist) == len(checklist):
        return True
    else:
        #print("INVALID")
        return False

def solve_part_two(input):
    """
    Solver for part two.
    """

    solution = 0

    for test in input:
        test = test.rstrip()
        #print("testing: "+test)
        if validate(test):
            if validate_anagrams(test):
                solution += 1

    return solution

def validate_anagrams(passphrase):
    """
    Checks a single passphrase for anagrams; returns true if it has none, false
    otherwise.
    """

    wordlist = passphrase.split()
    #print(wordlist)

    for word in wordlist:
        #print("comparing: "+word)
        for check in wordlist:
            #print("     to: "+check)
            if word == check:
                #print("...skip self compare...")
                pass
            elif is_anagram(word, check):
                return False

    return True

def is_anagram(a, b):
    """
    Checks if two words are anagrams of each other; returns true if so.
    """

    if len(a) != len(b):
        #print("not anagram: not the same length")
        return False
    else:
        a_list = sorted(list(a))
        b_list = sorted(list(b))

        #print(a_list)
        #print(b_list)

        if a_list == b_list:
            #print("anagram found")
            return True
        else:
            #print("no anagram found")
            return False

if __name__ == '__main__':
    sys.exit(main())

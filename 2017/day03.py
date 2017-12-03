#!/usr/bin/python3

"""
AOC 2017 Day 3:
    Wow! This was pretty cool; for part one, I banged my head against the table
    until I figured out how to actually just traverse the entire square and
    build a coordinate table. For part two, I tried to do that, but got lost in
    the weeds because it was getting super complicated; I remembered python's
    dict.get() method, and realized that by providing 0s for untraversed
    squares, I'd never need to figure out which neighbors have actually been
    generated.

    An alternate part 2 idea I had was to generate all neighbors, then discard
    the ones with a lower index than the current square, but that seemed like
    more work once I started writing the code.

    Also, part 2 was like 95% thumbtyped on my phone under the covers, again. I
    swear to god, this is going to be a theme for the month, that I'll give up
    and go to bed but think of a solution once I'm in bed and not want to get
    up again, but also won't be able to sleep until I finish it.
"""

import sys

COORD_TABLE = [(0,0)]

def main():
    """
    Main entry point.
    """

    # process input file

    inputfile = open(sys.argv[1], 'r')
    input = []
    for line in inputfile:
        input.append(line)
    inputfile.close()
    number = int(input[0].rstrip())

    # generate solutions

    print("part one solution: " + str(solve_part_one(number)))
    print("part two solution: " + str(solve_part_two(number)))

    return 0

def solve_part_one(input):
    """
    Solver for part one.
    """

    (x,y) = coords_of(input)
    #print((x,y))
    return  manhattan_distance((0,0), (x,y))

def coords_of(number):
    """
    Memoization for generating a global coordinate table for each index. If
    that index hasn't been generated yet, traverse the square until it is;
    otherwise, just perform a lookup.
    """

    global COORD_TABLE

    if number < len(COORD_TABLE):
        return COORD_TABLE[number]

    x = 0
    y = 0

    square = 1
    i = 1
    move = -1
    dir_counter = 0
    step = 1

    while i < number:
        #print(str(i) + ": " + str((x,y)))
        COORD_TABLE.append((x,y))

        turn = False

        if x == y:
            turn = True
            move *= -1
            dir_counter += 1
            step = 1
            y += move

        elif step <= dir_counter:
            y += move
        else:
            x += move

        step += 1
        i += 1
    #print(COORD_TABLE)
    return (x,y)

def manhattan_distance(start, end):
    """
    I scraped this off a stackexchange post for generating the manhattan
    distance >_>
    """

    sx, sy = start
    ex, ey = end

    return abs(ex - sx) + abs(ey - sy)

def solve_part_two(input):
    """
    Solver for part two.
    """

    solution = 0

    i = 1

    while gen_sequence(i) < input:
        i += 1

    return gen_sequence(i)

def neighbors(coord):
    """
    Generates all adjacent coordinates for the given tuple coordinate.
    """

    (x,y) = coord

    return [(x, y+1),
            (x+1,y+1),
            (x+1,y),
            (x+1,y-1),
            (x,y-1),
            (x-1,y-1),
            (x-1,y),
            (x-1,y+1)]

def gen_sequence(max_square):
    """
    Generates part two sequence up to the given max square; this function takes
    all neighbors of the given square and sums their values, and if a square
    hasn't been traversed yet, its value defaults to 0.
    """

    if max_square <= 2:
        return 1
    else:
        value_table = {(0,0): 1,
                (0,1):1}
        n = 3
        while n <= max_square:
            value = 0
            #print("calc "+str(n))
            here = coords_of(n)
            neighborhood = neighbors(here)
            #print(neighborhood)
            for item in neighborhood:
                add = value_table.get(item, 0)
                #print("adding " +str(add))
                value += add
                #value += value_table.get(item, 0)
            value_table.update({here:value})
            n += 1
            #print(value)

    #print(value_table)

    return value

if __name__ == '__main__':
    sys.exit(main())

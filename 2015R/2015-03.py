#!/usr/bin/python3

def move(start, direction):
    if x == "^":
        return(start[0]+1, start[1])
    elif x == ">":
        return(start[0], start[1]+1)
    elif x == "<":
        return(start[0], start[1]-1)
        j-=1
    else:
        return(start[0]-1, start[1])

i,j = (0,0)
locations = {(0,0): True}

for x in list(open("2015-03-input.txt").readline()):
    (i,j) = move((i,j), x)
    locations.update({(i,j): True})

print(len(locations.keys()))

i,j = (0,0)
p,q = (0,0)
turn = 0
locations = {(0,0): True}

for x in list(open("2015-03-input.txt").readline()):
    if turn % 2 == 0:
        i,j = move((i,j), x)
    else:
        p,q = move((p,q), x)

    locations.update({(i,j): True, (p,q): True})
    turn += 1

print(len(locations.keys()))

#!/usr/bin/python3

i,j = (0,0)
locations = {(0,0): True}

for x in list(open("2015-03-input.txt").readline()):
    if x == "^":
        i+=1
    elif x == ">":
        j+=1
    elif x == "<":
        j-=1
    else:
        i-=1

    locations.update({(i,j): True})

print(len(locations.keys()))

i,j = (0,0)
p,q = (0,0)
turn = 0
locations = {(0,0): True}

for x in list(open("2015-03-input.txt").readline()):
    if turn % 2 == 0:
        a,b = i,j
    else:
        a,b = p,q

    if x == "^":
        a+=1
    elif x == ">":
        b+=1
    elif x == "<":
        b-=1
    else:
        a-=1


    if turn % 2 == 0:
        i,j = a,b
    else:
        p,q = a,b

    locations.update({(a,b): True})
    turn += 1

print(len(locations.keys()))

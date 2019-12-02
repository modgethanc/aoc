#!/usr/bin/python3

paper = 0
ribbon = 0

for x in open("2015-02-input.txt").readlines():
    d = list(map(int, x.rstrip().split('x')))
    d.sort()
    paper += 2*(d[0]*d[1]+ d[1]*d[2] + d[0]*d[2]) + d[0]*d[1]

print(paper)
print(ribbon)

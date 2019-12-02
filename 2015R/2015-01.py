#!/usr/bin/python3

ans = 0
count = 0

for x in list(open("2015-01-input.txt").readline()):
    if ans == -1:
        print(count)
    if x == '(':
        ans += 1
    else:
        ans -= 1
    count += 1

print(ans)

import re
import os

input = open("input.txt").read().split("\n\n")

machines = []

total = 0

for part in input:
    ax, ay, bx, by, px, py = list(map(int, re.findall(r"\d+", part)))
    px += 10000000000000
    py += 10000000000000
    pushA = (px*by - py*bx)/(ax*by - ay*bx)
    pushB = (px - ax*pushA)/(bx)
   # print(pushA, pushB)
    if pushA % 1 == 0 and pushB % 1 == 0:
        total += (3*pushA + pushB)

print(int(total))

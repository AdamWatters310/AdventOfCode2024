import re

input = open("input.txt").read().splitlines()
DISTANCE = 100
WIDTH = 101
HEIGHT = 103

finalpostiions = []
quadrants = [0, 0, 0, 0]

for line in input:
    x, y, dx, dy = map(int, re.findall(r"-*\d+", line))
    for _ in range(DISTANCE):
        x += dx
        y += dy
        x %= WIDTH
        y %= HEIGHT

    if x < WIDTH//2:
        if y < HEIGHT//2:
            quadrants[0]+=1
        elif y > HEIGHT//2:
            quadrants[3]+=1
    elif x > WIDTH//2:
        if y < HEIGHT//2:
            quadrants[1]+=1
        elif y > HEIGHT//2:
            quadrants[2]+=1

print(quadrants)

safety = 1
for q in quadrants:
    safety *= q

print(safety)

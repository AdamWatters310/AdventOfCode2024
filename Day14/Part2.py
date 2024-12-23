import re

inputa = open("input.txt").read().splitlines()
WIDTH = 101
HEIGHT = 103
iterations = 0

START_POS = 5000

finalpostiions = []
quadrants = [0, 0, 0, 0]

locations = []
velocities = []

grid = []
for _ in range(HEIGHT):
    grid += [[" " for _ in range(WIDTH)]]

for line in inputa:
    x, y, dx, dy = map(int, re.findall(r"-*\d+", line))
    locations.append([x, y])
    velocities.append([dx, dy])

def movetimes(times):
    global iterations
    for i in range(len(locations)):
        for _ in range(times):
            locations[i][0] += velocities[i][0]
            locations[i][1] += velocities[i][1]
            locations[i][0] %= WIDTH
            locations[i][1] %= HEIGHT
    iterations += times

def makegrid():
    for location in locations:
        grid[location[1]][location[0]] = "#"
    for r in range(HEIGHT):
        for c in range(WIDTH):
            print(grid[r][c], end="")
        print("\n", end="")
    print("AFTER", iterations)

def cleargrid():
    for r in range(HEIGHT):
        for c in range(WIDTH):
            grid[r][c] = " "



movetimes(START_POS)

while(True):
    movetimes(1)
    makegrid()
    cleargrid()
    _ = input()

#userinput = "1"
#while userinput != 0:
#    userinput = input("How Many Iterations?")
#    if userinput == "":
#        userinput = "1"
#    movetimes(int(userinput))
#    cleargrid()
#    makegrid()
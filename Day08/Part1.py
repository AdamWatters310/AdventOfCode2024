inputStr = open("input.txt").read().splitlines()

grid = []

for line in inputStr:
    grid.append(list(line))

locations = []

def writecell(r, c, val):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return
    grid[r][c] = val

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != '.':
            locations.append([r, c, grid[r][c]])

for location1 in locations:
    for location2 in locations:
        if location1 == location2: continue
        if location1[2] == location2[2]:
            writecell(location1[0]-(location2[0]-location1[0]), location1[1]-(location2[1]-location1[1]), '@')

total = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            total += 1

print(total)
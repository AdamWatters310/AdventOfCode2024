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
            dr = (location2[0]-location1[0])
            dc = (location2[1]-location1[1])
            cr = location1[0]
            cc = location1[1]
            while cr > 0 and cc > 0 and cr < len(grid) and cc < len(grid):
                cr -= dr
                cc -= dc
                writecell(cr, cc, '@')
            cr = location1[0]
            cc = location1[1]
            while cr > 0 and cc > 0 and cr < len(grid) and cc < len(grid):
                cr += dr
                cc += dc
                writecell(cr, cc, '@')


total = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            total += 1

print(total)
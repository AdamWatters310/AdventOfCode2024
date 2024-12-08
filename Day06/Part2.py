strs = open("input.txt").read().splitlines()
runningtotal = 0

grid = []

for str in strs:
    grid.append(list(str))

def findGuard(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                return (r, c)
    return (-2, -2)
            
def turnGuard(dr, dc):
    if (dr, dc) == (-1, 0): return (0, 1)
    elif (dr, dc) == (0, 1): return (1, 0)
    elif (dr, dc) == (1, 0): return (0, -1)
    elif (dr, dc) == (0, -1): return (-1, 0)
    else:
        print("Error: bad directions set ", (dr, dc))
        return (-1, 0)

def checkcell(r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 'X'
    return grid[r][c]

def checkWall(gr, gc, dr, dc):
    if checkcell(gr+dr, gc+dc) == '#': return True
    return False


def hasloop(gr, gc):
    visited = set()
    (dr, dc) = (-1, 0)
    while not (gr < 0 or gr >= len(grid) or gc < 0 or gc >= len(grid[0])):
        if (gr, gc, dr, dc) in visited: 
            return True
        visited.add((gr, gc, dr, dc))
        while checkWall(gr, gc, dr, dc): (dr, dc) = turnGuard(dr, dc)
        gr += dr
        gc += dc
    return False

(gr, gc) = findGuard(grid)
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '.':
            grid[r][c] = '#'
            if hasloop(gr, gc): 
#                print("Loop at ", (r, c))
                runningtotal += 1
            grid[r][c] = '.'
    print("Finished row ", r)

print(runningtotal)
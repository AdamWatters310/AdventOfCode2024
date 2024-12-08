grid = open("input.txt").read().splitlines()

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

visited = set()

(gr, gc) = findGuard(grid)
(dr, dc) = (-1, 0)
while not (gr < 0 or gr >= len(grid) or gc < 0 or gc >= len(grid)):
    visited.add((gr, gc))
    if checkWall(gr, gc, dr, dc): (dr, dc) = turnGuard(dr, dc)
    gr += dr
    gc += dc

print(len(visited))
gridstr, dirs = open("input.txt").read().split("\n\n")

grid = []
rr = 0
rc = 0

directions = {}
directions['^'] = [-1, 0]
directions['v'] = [1, 0]
directions['<'] = [0, -1]
directions['>'] = [0, 1]

for line in gridstr.splitlines():
    grid.append(list(line))

def checkcell(r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return -1
    return grid[r][c]

# returns true if able to move, false otherwise
def trymove(r, c, dir):
    charmoving = checkcell(r, c)
    charatmovepos = checkcell(r+dir[0], c+dir[1])
#    print(charmoving, charatmovepos)
    if charmoving == '#' or charatmovepos == '#' or charatmovepos == -1:
        return False
    elif charatmovepos =='.':
        grid[r][c] = '.'
        grid[r+dir[0]][c+dir[1]] = charmoving
        return True
    elif charatmovepos == 'O':
        if trymove(r+dir[0], c+dir[1], dir):
            grid[r][c] = '.'
            grid[r+dir[0]][c+dir[1]] = charmoving
            return True
        else:
            return False
    print("ERROR: trymove failed to determine next step", r, c, dir, charatmovepos)
    return False
    
    

def findrobot():
    global rr, rc
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                rr = r
                rc = c

for inst in dirs:
    if inst=="\n": continue
    findrobot()
    dir = directions[inst]
    trymove(rr, rc, dir)
#    print("Finished a move")

total = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'O':
            total += ((r*100) + c)


print(total)
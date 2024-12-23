from collections import deque
inputf = open("input.txt").read().splitlines()
bytespos = []
for line in inputf:
    bytespos.append(list(map(int, line.split(','))))
print(bytespos)
ENDC = 70
LIMIT = 2959
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

bytespos = bytespos[:LIMIT]

bfsqueue = deque()

visited = set()

def bfs(level, dir, pos):
    if((dir[0], dir[1], pos[0], pos[1])) in visited:
        return -1
    visited.add((dir[0], dir[1], pos[0], pos[1]))
    if pos[0] < 0 or pos[1] < 0 or pos[0] > ENDC or pos[1] > ENDC:
        return -1
    if pos in bytespos:
        return -1
    if pos == [ENDC, ENDC]:
        return level
    for gdir in dirs:
        if gdir != [dir[0]*-1, dir[1]*-1]:
            bfsqueue.append((level+1, gdir, [pos[0]+dir[0], pos[1]+dir[1]]))
    return -1

bfsqueue.append((0, [0,0], [0,0]))

while len(bfsqueue):
    level, dir, pos = bfsqueue.popleft()
    res = bfs(level, dir, pos)
    if res != -1:
        print(level-1)
        break
#    print(bfsqueue)
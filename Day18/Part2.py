from collections import deque
import math
inputf = open("input.txt").read().splitlines()
bytesposg = []
for line in inputf:
    bytesposg.append(list(map(int, line.split(','))))
ENDC = 70
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def p1sol(limit):
    global ENDC, dirs, bytesposg
    bytespos = bytesposg[:limit]
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
            return True
    return False

s = 0
e = len(bytesposg)
while s < e:
    mid = math.ceil((s+e)/2)

    print((s, e))
    if p1sol(mid):
        s = mid
    else:
        e = mid-1

print(s)
import sys

grid = [list(line) for line in open("input.txt").read().splitlines()]

sys.setrecursionlimit(2000)

sr, sc = 0, 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            sr = r
            sc = c

costs = [[-1]*(len(grid[0])) for _ in range(len(grid))]

r = sr
c = sc
costs[r][c] = 0
while grid[r][c] != "E":
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): continue
        if grid[nr][nc] == "#": continue
        if costs[nr][nc] != -1: continue
        costs[nr][nc] = costs[r][c] + 1
        r = nr
        c = nc

for row in costs:
    print(*row, sep="\t")

count = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '#': continue
        for dr, dc in [(2, 0), (1, 1), (0, 2), (-1, 1)]:
            nr = r+dr
            nc = c+dc
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): continue
            if costs[nr][nc] == -1: continue
            if abs(costs[nr][nc] - costs[r][c]) >= 102:
                count+=1

print(count)

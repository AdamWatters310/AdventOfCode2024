import heapq

grid = [list(line.strip()) for line in open("input.txt").read().splitlines()]

sr, sc = 0, 0
er, ec = 0, 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            sr = r
            sc = c
        elif grid[r][c] == 'E':
            er = r
            ec = c

# nodes identified by row, col, and direction
pq = [(0, sr, sc, 0, 1)]
seen = set()

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    seen.add((r, c, dr, dc))
    if (r, c) == (er, ec):
        print(cost)
        break
    for (ncost, nr, nc, ndr, ndc) in [(cost+1, r+dr, c+dc, dr, dc), (cost+1000, r, c, -dc, dr), (cost+1000, r, c, dc, -dr)]:
        if grid[nr][nc] == '#': continue
        if (nr, nc, ndr, ndc) in seen: continue
        
        heapq.heappush(pq, (ncost, nr, nc, ndr, ndc))

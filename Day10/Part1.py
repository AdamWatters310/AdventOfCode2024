input = open("input.txt").read().splitlines()

grid = []

for i in range(len(input)):
    grid.append(list(map(int, list(input[i]))))

visited = set()

def checkcell(r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return -1
    return grid[r][c]

# returns the number of ways of making it to a 9 from here
def dfs(step, r, c):
    visited.add((r, c))
    if step >= 9:
        return 1
    rt = 0
    if checkcell(r+1, c) == step+1 and (r+1, c) not in visited: rt += dfs(step+1, r+1, c)
    if checkcell(r-1, c) == step+1 and (r-1, c) not in visited: rt += dfs(step+1, r-1, c)
    if checkcell(r, c+1) == step+1 and (r, c+1) not in visited: rt += dfs(step+1, r, c+1)
    if checkcell(r, c-1) == step+1 and (r, c-1) not in visited: rt += dfs(step+1, r, c-1)
    return rt


total = 0
for r in range(len(grid)):
    for c in range(len(grid)):
        if grid[r][c] == 0: 
            visited = set()
            total += dfs(0, r, c)

print(total)
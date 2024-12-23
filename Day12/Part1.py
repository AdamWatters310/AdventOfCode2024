input = open("input.txt").read().splitlines()

perims = []
total = 0
visited = set()
endvals = []

def checkcell(r, c):
    if r < 0 or r >= len(input) or c < 0 or c >= len(input[0]):
        return -1
    return input[r][c]

def dfsArea(r, c):
    if (r, c) in visited:
        return [0, 0] # don't double count
    visited.add((r, c))
    ch = input[r][c]
    area = 1 
    perimeter = 0
    if checkcell(r+1, c) == ch:
        outp = dfsArea(r+1, c)
        area += outp[0]
        perimeter += outp[1]
    else:
        perimeter += 1
    if checkcell(r-1, c) == ch:
        outp = dfsArea(r-1, c)
        area += outp[0]
        perimeter += outp[1]
    else:
        perimeter += 1
    if checkcell(r, c+1) == ch:
        outp = dfsArea(r, c+1)
        area += outp[0]
        perimeter += outp[1]
    else:
        perimeter += 1
    if checkcell(r, c-1) == ch:
        outp = dfsArea(r, c-1)
        area += outp[0]
        perimeter += outp[1]
    else:
        perimeter += 1
    return [area, perimeter]

for i in range(len(input)):
    perims += [[0 for _ in range(len(input[0]))]]

for r in range(len(input)):
    for c in range(len(input[0])):
        if not ((r, c) in visited):
            endvals.append(dfsArea(r, c))

for i in range(len(endvals)):
    total += (endvals[i][0] * endvals[i][1])

print(total)

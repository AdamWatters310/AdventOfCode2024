input = open("input.txt").read().splitlines()

perims = []
total = 0
visited = set()
endvals = []
thisIter = set()

asum = 0

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def checkcell(r, c):
    if r < 0 or r >= len(input) or c < 0 or c >= len(input[0]):
        return -1
    return input[r][c]

def dfsArea(r, c):
    if (r, c) in visited:
        return 0
    thisIter.add((r, c))
    visited.add((r, c))
    ch = input[r][c]
    area = 1 
    if checkcell(r+1, c) == ch:
        area += dfsArea(r+1, c)
    if checkcell(r-1, c) == ch:
        area += dfsArea(r-1, c)
    if checkcell(r, c+1) == ch:
        area += dfsArea(r, c+1)
    if checkcell(r, c-1) == ch:
        area += dfsArea(r, c-1)
    return area

for i in range(len(input)):
    perims += [[0 for _ in range(len(input[0]))]]

for r in range(len(input)):
    for c in range(len(input[0])):
        if not ((r, c) in visited):
            thisIter = set()
            area = dfsArea(r, c)
            if checkcell(r, c) == 'P' and area == 1:
                print("Found P of size one at", r, c)
            asum += area

            tcorners = 0
            for (nr, nc) in thisIter:
                corners = 0
                borders = [(checkcell(nr+dir[0], nc+dir[1]) == checkcell(nr, nc)) for dir in dirs]
                bc = sum(borders)
                if bc == 0:
                    corners = 4
                if bc == 1:
                    corners += 2
                elif bc == 2:
                    if not (borders == [True, False, True, False] or borders == [False, True, False, True]):   
                        corners += 1
                    if borders == [False, True, True, False] and checkcell(nr+1, nc+1)!=checkcell(nr, nc): corners+=1
                    elif borders == [False, False, True, True] and checkcell(nr+1, nc-1)!=checkcell(nr, nc): corners+=1
                    elif borders == [True, False, False, True] and checkcell(nr-1, nc-1)!=checkcell(nr, nc): corners+=1
                    elif borders == [True, True, False, False] and checkcell(nr-1, nc+1)!=checkcell(nr, nc): corners+=1
                elif bc == 3:
                    if borders == [True, True, True, False]:
                        corners += (checkcell(nr, nc)!=checkcell(nr-1, nc+1))
                        corners += (checkcell(nr, nc)!=checkcell(nr+1, nc+1))
                    elif borders == [False, True, True, True]:
                        corners += (checkcell(nr, nc)!=checkcell(nr+1, nc+1))
                        corners += (checkcell(nr, nc)!=checkcell(nr+1, nc-1))
                    elif borders == [True, False, True, True]:
                        corners += (checkcell(nr, nc)!=checkcell(nr-1, nc-1))
                        corners += (checkcell(nr, nc)!=checkcell(nr+1, nc-1))
                    elif borders == [True, True, False, True]:
                        corners += (checkcell(nr, nc)!=checkcell(nr-1, nc-1))
                        corners += (checkcell(nr, nc)!=checkcell(nr-1, nc+1))
                elif bc == 4:
                    diagonals = [checkcell(nr, nc)!=checkcell(nr+d[0], nc+d[1]) for d in [[-1, -1], [-1, 1], [1, -1], [1, 1]]]
                    corners += sum(diagonals)
                tcorners += corners
            #    print("Corners at", r, c, "is", corners)
            total += (area * tcorners)
        #    print(checkcell(r, c), area, tcorners)

print(asum)

print(total)

input = open("input.txt").read().splitlines()

def checkcell(r, c, ch):
    if r >= len(input) or r < 0 or c >= len(input[0]) or c < 0:
        return False
    return input[r][c] == ch

def checkSeq(r, c, dr, dc):
    return checkcell(r+dr, c+dc, 'M') and checkcell(r+2*dr, c+2*dc, 'A') and checkcell(r+3*dr, c+3*dc, 'S')

runningtotal = 0
for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c] == 'X':
            for (dr,dc) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if checkSeq(r, c, dr, dc):
                    runningtotal += 1

print(runningtotal)


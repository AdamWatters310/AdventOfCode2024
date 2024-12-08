input = open("input.txt").read().splitlines()

def checkcell(r, c, ch):
    if r >= len(input) or r < 0 or c >= len(input[0]) or c < 0:
        return False
    return input[r][c] == ch

runningtotal = 0
for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c] == 'A':
            if (checkcell(r-1, c-1, 'M') and checkcell(r+1, c+1, 'S')) or (checkcell(r-1, c-1, 'S') and checkcell(r+1, c+1, 'M')):
                if (checkcell(r-1, c+1, 'M') and checkcell(r+1, c-1, 'S')) or (checkcell(r-1, c+1, 'S') and checkcell(r+1, c-1, 'M')):
                    runningtotal += 1
print(runningtotal)


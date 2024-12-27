ins = open("input.txt").read().split("\n\n")
keys = []
locks = []

for block in ins:
    res = []
    lines = block.splitlines()
    firstch = lines[0][0]
    for x in range(len(lines[0])):
        count = 0
        for y in range(len(lines)):
            if lines[y][x] == '#':
                count+=1
        res.append(count)
    if firstch=='#':
        locks.append(res)
    else:
        keys.append(res)

#print(locks)
#print(keys)

finaltotal = 0
for lock in locks:
    for key in keys:
        valid = True
        for i in range(len(lock)):
            if lock[i]+key[i] > 7:
                valid=False
        if valid:
            finaltotal += 1

print(finaltotal)
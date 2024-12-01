input = open("input.txt").read().splitlines()

leftlist = []
rightlist = []
for line in input :
    l, r = line.split("   ")
    leftlist.append(int(l))
    rightlist.append(int(r))

leftlist.sort()
rightlist.sort()

runningtotal = 0
for i in range(len(leftlist)):
    runningtotal += (leftlist[i]) * rightlist.count(leftlist[i])

print(runningtotal)

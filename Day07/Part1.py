def applyOperation(ls, ops):
    total = ls[0]
    for i in range(1, len(ls)):
        if ops%2 == 0:
            total += ls[i]
        else:
            total *= ls[i]
        ops //= 2
    return total

input = open("input.txt").read().splitlines()

runningtotal = 0
lineno = 0
for line in input:
    testVal, tail = line.split(":")
    testVal = int(testVal)
    vals = list(map(int, tail.strip().split()))
    for ops in range(pow(2, len(vals)-1)):
        if applyOperation(vals, ops) == testVal:
            runningtotal += testVal
        #    print("list ", vals, "ops ", ops)
            break
    lineno += 1
    print("Finished line ", lineno)

print(runningtotal)
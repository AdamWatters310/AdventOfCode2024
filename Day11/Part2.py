input = open("input.txt").read().split()

# val -> [[vals], steps to get there]
cache = {}
ITERATIONS = 75

def getStoneCount(iter, val):
    if iter == ITERATIONS:
        return 1
    if (iter, val) in cache: return cache[(iter, val)]
    returnVal = 0
    sval = str(val)
    if val == 0: 
        returnVal = getStoneCount(iter+1, 1)
    elif len(sval) % 2 == 0: 
        returnVal = getStoneCount(iter+1, int(sval[:(len(sval)//2)])) + getStoneCount(iter+1, int(sval[(len(sval)//2):]))
    else :
        returnVal = getStoneCount(iter+1, val*2024)
    cache[(iter, val)] = returnVal
    return returnVal

total = 0
for val in input:
    total += getStoneCount(0, int(val))
    print("Finished a stone!")

print(total)
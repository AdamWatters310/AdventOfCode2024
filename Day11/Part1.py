input = open("input.txt").read().split()

# val -> [[vals], steps to get there]
cache = {}
ITERATIONS = 25

def getStoneCount(iter, val):
    if (iter, val) in cache: return cache[(iter, val)]
    if iter == ITERATIONS:
        return 1
    if val == 0: return getStoneCount(iter+1, 1)
    sval = str(val)
    if len(sval) % 2 == 0: return getStoneCount(iter+1, int(sval[:(len(sval)//2)])) + getStoneCount(iter+1, int(sval[(len(sval)//2):]))
    return getStoneCount(iter+1, val*2024)

total = 0
for val in input:
    total += getStoneCount(0, int(val))

print(total)
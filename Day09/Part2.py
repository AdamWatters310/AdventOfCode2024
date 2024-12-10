input = open("input.txt").read()

blocks = []
id = 0
lin = len(input)

for i in range(len(input)):
    if i%2==1:
        blocks += [[-1 for a in range(int(input[i]))]]
    else:
        blocks += [[id for a in range(int(input[i]))]]
        id += 1

leftBase = 1 #point to the first empty block
rightBase = len(blocks)-1

while rightBase > 0:
    leftBase = 1

    while not (len(blocks[leftBase]) > 0 and blocks[leftBase][0]==-1): leftBase += 1
    while not (len(blocks[rightBase]) > 0 and blocks[rightBase][0] != -1): rightBase -= 1
#    print("Searching for somewhere to put ", blocks[rightBase], "starting from", leftBase, "at block", blocks[leftBase])
#    print("state of blocks: ", blocks)
    if leftBase >= rightBase:
        rightBase -= 1
        continue
    left = leftBase
    while left < rightBase and not (len(blocks[left]) >= len(blocks[rightBase]) and blocks[left][0]==-1): 
        #print(left, rightBase)
        
        left += 1
    if left >= rightBase: 
        rightBase -= 1
        continue
#    print("Moved left pointer up to", left, ", now pointing at block", blocks[left])
    blocks.insert(left, [(blocks[rightBase][0]) for i in range(len(blocks[rightBase]))])
    left += 1
    rightBase += 1  #update both pointers to account for array modification 
    blocks[left] = blocks[left][(len(blocks[rightBase])):]
    for i in range(len(blocks[rightBase])):
        blocks[rightBase][i] = -1

#    print("Before merge", blocks)
    for i in range(len(blocks)-1):
        if len(blocks[i]) > 0 and len(blocks[i+1]) > 0:
            if blocks[i][0]==-1 and blocks[i+1][0] == -1:
                blocks[i+1] += [-1 for a in range(len(blocks[i]))]
                blocks[i] = []
#    print("After merge", blocks)
    print((lin-rightBase)/lin)

position = 0
total = 0

for i in range(len(blocks)):
    for j in range(len(blocks[i])):
        if blocks[i][j] != -1:
            total += position*blocks[i][j]
        position += 1

print(total)
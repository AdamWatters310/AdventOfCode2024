input = open("input.txt").read()

blocks = []
id = 0

for i in range(len(input)):
    if i%2==1:
        blocks += [-1 for a in range(int(input[i]))]
    else:
        blocks += [id for a in range(int(input[i]))]
        id += 1

right = len(blocks)-1
left = 0

while right > left:
    while blocks[right] == -1: right -= 1
    while blocks[left] != -1: left += 1
    if right <= left: break
    blocks[left] = blocks[right]
    blocks[right] = -1

total = 0
for i in range(len(blocks)):
    if blocks[i] != -1:
        total += (blocks[i] * i)


print(total)
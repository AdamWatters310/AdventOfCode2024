prog = list(map(int, open("input.txt").read().split(",")))
bits = 0
output = 0

for i in range(len(prog)):
    current = prog[i]
    current ^= 1
    output += (current << bits)
    bits += 3

print(output)
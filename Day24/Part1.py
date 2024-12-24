initial, finput = open("input.txt").read().split("\n\n")
vals = {}

knownvals = {}

#rule format output -> (in1 OP in2)
rules = {}

for val in initial.splitlines():
    k, v = val.split(": ")
    vals[k] = int(v)
    knownvals[k] = int(v)

operators = {
    "OR": lambda x, y: x|y,
    "AND": lambda x, y: x&y,
    "XOR": lambda x, y: x^y,
}

def solve(wire):
    if wire in knownvals:
        return knownvals[wire]
    in1, op, in2 = rules[wire]
    knownvals[wire] = operators[op](solve(in1), solve(in2))
    return knownvals[wire]
    
for line in finput.splitlines():
    in1, op, in2, outp = line.replace(" -> ", " ").split()
    rules[outp] = (in1, op, in2)

i = 0
z = []
while True:
    key = "z" + str(i).rjust(2, "0")
    if key not in rules: break
    z.append(solve(key))
    i += 1

print(int("".join(map(str, z[::-1])), 2))



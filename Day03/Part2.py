import re

input = open("input.txt").read()

runningtotal = 0
muls = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", input)
enabled = True
for mul in muls:
    if mul == "don't()":
        enabled = False
    elif mul == "do()":
        enabled = True
    elif enabled:
        vals = list(map(int, re.findall(r"\d+", mul)))
        print(vals)
        runningtotal += vals[0]*vals[1]
print(runningtotal)
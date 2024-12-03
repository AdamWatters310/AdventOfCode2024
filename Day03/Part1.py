import re

input = open("input.txt").read()

runningtotal = 0
muls = re.findall(r"mul\(\d+,\d+\)", input)
for mul in muls:
    vals = list(map(int, re.findall(r"\d+", mul)))
    runningtotal += vals[0]*vals[1]
print(runningtotal)
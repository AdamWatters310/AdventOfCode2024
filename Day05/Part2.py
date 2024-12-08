from functools import cmp_to_key

input = open("input.txt").read().splitlines()

rules = []
seq = []

rule_cache = {}

runningtotal = 0

for line in input:
    if "|" in line:
        rules.append(list(map(int, line.split("|"))))
    elif "," in line:
        seq.append(list(map(int, line.split(","))))

for rule in rules:
    rule_cache[(rule[0], rule[1])] = -1
    rule_cache[(rule[1], rule[0])] = 1

def compare(a, b):
    if (a, b) in rule_cache:
        return rule_cache[(a, b)]
    return 0

def isvalid(sequence):
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if compare(sequence[i], sequence[j]) == 1:
                return False
    return True  

for s in seq:
    if not isvalid(s):
    #    print(s)
        ss = sorted(s, key=cmp_to_key(compare))
        runningtotal += (ss[len(ss)//2])
    #    print(ss)

print(runningtotal)
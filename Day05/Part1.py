input = open("input.txt").read().splitlines()

rules = []
seq = []

runningtotal = 0

for line in input:
    if "|" in line:
        rules.append(list(map(int, line.split("|"))))
    elif "," in line:
        seq.append(list(map(int, line.split(","))))

for s in seq:
    currentrules = []
    for r in rules:
        if r[0] in s and r[1] in s: currentrules.append((r[0], r[1]))
    valid = True
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if (s[j], s[i]) in currentrules:
                valid = False
            #print(s, " invalid as breaks rule ", b, a)
    if valid: 
        runningtotal += s[int(len(s)//2)]
        print(s, " valid with ruleset ", currentrules)    

print(runningtotal)

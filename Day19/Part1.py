designs_str, patterns_str = open("input.txt").read().split("\n\n")

patterns = patterns_str.splitlines()
designs = designs_str.split(", ")

knowndesigns = {}

def searchdesign(pattern):
    global designs, knowndesigns
    if pattern in knowndesigns:
        return knowndesigns[pattern]
    if len(pattern) <= 0:
        return 1
    outp = 0
    for design in designs:
        if pattern.startswith(design):
            out = searchdesign(pattern[len(design):])
            if out != 0:
                knowndesigns[pattern] = out
                outp += out
    knowndesigns[pattern] = outp
    return outp

total = 0
for pattern in patterns:
    if searchdesign(pattern):
        total +=1
print(total)

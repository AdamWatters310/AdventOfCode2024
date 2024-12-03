    
def checkline(line):
    diffs = [x-y for (x, y) in zip(line, line[1:])]
    return all(d >= 1 and d <= 3 for d in diffs) or all(d <= -1 and d >= -3 for d in diffs)

input = open("input.txt").read().splitlines()
running_total = 0
for line in input :
    line_in = list(map(int, line.split()))
    if any(checkline(line_in[:index]+line_in[index+1:]) for index in range(len(line_in))):
        running_total+=1

print(running_total)
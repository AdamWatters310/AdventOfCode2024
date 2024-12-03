input = open("input.txt").read().splitlines()

running_total = 0
for line in input :
    is_valid = True
    direction = 0
    line_ins = line.split()
    line_ins = list(map(int, line_ins))
    for i in range(len(line_ins)-1):
        line_diff = line_ins[i+1] - line_ins[i]
        if direction == 0 and line_diff != 0:
            direction = line_diff / abs(line_diff)
        is_valid = is_valid and (line_diff*direction) >=1 and (line_diff*direction) <= 3
    if is_valid:
        running_total += 1

print(running_total)
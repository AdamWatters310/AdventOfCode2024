invals = list(map(int, open("input.txt").read().splitlines()))

def next_num(current):
    secret = current
    temp = current * 64
    secret ^= temp
    secret = secret % 16777216
    temp = int(secret / 32)
    secret ^= temp
    secret %= 16777216
    temp = secret * 2048
    secret ^= temp
    secret %= 16777216
    return secret

total = 0
for val in invals:
    cv = val
    for i in range(2000):
        cv = next_num(cv)
    total += cv

print(total)


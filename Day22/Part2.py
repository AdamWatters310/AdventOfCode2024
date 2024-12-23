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

seqtotals = {}

total = 0
for val in invals:
    cv = val
    prices = [cv%10]
    seen = set()
    for i in range(2000):
        cv = next_num(cv)
        prices.append(cv%10)
    for i in range(len(prices)-4):
        a, b, c, d, e = prices[i:(i+5)]
        seq = (b-a, c-b, d-c, e-d)
        if seq in seen: continue
        seen.add(seq)
        if seq not in seqtotals:
            seqtotals[seq] = 0
        seqtotals[seq] += e

print(max(seqtotals.values()))

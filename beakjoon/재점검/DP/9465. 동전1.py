import sys

N, G = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
DP = [0 for _ in range(G + 1)]
DP[0] = 1
for coin in coins:
    for g in range(1, G + 1):
        if g - coin >= 0:
            DP[g] += DP[g - coin]

print(DP[-1])
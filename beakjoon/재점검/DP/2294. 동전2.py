import sys

N, G = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

cnt = [sys.maxsize for _ in range(G + 1)]
cnt[0] = 0
for coin in coins:
    for g in range(1, G + 1):
        if g - coin >= 0:
            cnt[g] = min(cnt[g], cnt[g - coin] + 1)

print(cnt[-1] if cnt[-1] < sys.maxsize else -1)
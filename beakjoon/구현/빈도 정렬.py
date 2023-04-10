import sys
from collections import Counter
N, C = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
counter = {}
for idx, v in enumerate(sequence):
    if v in counter:
        counter[v][0] += 1
    else:
        counter[v] = [1, idx]
for v in sorted(list(counter.items()), key = lambda x: (-x[1][0], x[1][1])):
    for c in range(v[1][0]):
        print(v[0], end = ' ')
print()
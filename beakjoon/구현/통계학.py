import sys
import math
from collections import Counter
N = int(sys.stdin.readline())
L = []
for _ in range(N):
    L.append(int(sys.stdin.readline()))
L.sort()
print(round(sum(L)/len(L)))
print(L[len(L)//2])
counter = sorted(Counter(L).items(), key = lambda x: (-x[1], x[0]))
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])
print(L[-1] - L[0])
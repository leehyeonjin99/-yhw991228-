import itertools
import sys
N, M=map(int,sys.stdin.readline().split())
L=list(itertools.permutations(range(1, N+1), M))
for comb in L:
    for num in comb:
        print(num, end=' ')
    print()
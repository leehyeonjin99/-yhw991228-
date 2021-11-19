import sys

N=int(sys.stdin.readline())
L=list(map(int, sys.stdin.readline().split()))

S=sorted(list(set(L)))

'''for num in L:
    print(S.index(num), end=' ')'''

dic={S[i]:i for i in range(len(S))}
for num in L:
    print(dic[num], end=' ')
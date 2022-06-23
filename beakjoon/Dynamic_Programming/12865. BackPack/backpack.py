import sys
N, M=map(int,sys.stdin.readline().split())
L=[]
for i in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
'''
def value_sum(L):
    sum=0
    for l in L:
        sum+=l[1]
    return sum

def weight_sum(L):
    sum=0
    for l in L:
        sum+=l[0]
    return sum

import itertools
M=[]
for i in range(1,N+1):
    C=itertools.combinations(L,i)
    F=[]
    for c in C:
        if weight_sum(c)<=MW:
            F.append(value_sum(c))
    if F:
        M.append(max(F))
    else:
        break

print(max(M))
'''
VS=[[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if j>=L[i-1][0]:
            VS[i][j]=max(VS[i-1][j],VS[i-1][j-L[i-1][0]]+L[i-1][1])
        else:
            VS[i][j]=VS[i-1][j]

print(VS[-1][-1])
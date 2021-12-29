import sys
from itertools import combinations
N=int(sys.stdin.readline())
for i in range(N):
    M=int(sys.stdin.readline())
    L={}
    for j in range(M):
        name, kind=sys.stdin.readline().split()
        if kind in L.keys():
            L[kind].append(name)
        else:
            L[kind]=[name]
    '''result=0
    for i in range(len(L)):
        R=combinations(L.keys(),i+1)
        for rs in R:
            multi=1
            for r in rs:
                multi=multi*len(L[r])
            result+=multi
    print(result)'''
    R=[]
    for k in L.keys():
        R.append(len(L[k])+1)
    result=1
    for r in R:
        result=result*r
    print(result-1)
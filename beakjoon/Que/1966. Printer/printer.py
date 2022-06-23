import sys
num=int(sys.stdin.readline())
for i in range(num):
    N, M=map(int, sys.stdin.readline().split())
    L=list(map(int,sys.stdin.readline().split()))
    idx=list(range(len(L)))
    idx[M]='target'
    count=0
    finish=False
    while not finish:
        if L[0]==max(L):
            count+=1
            if idx[0]=='target':
                print(count)
                finish=True
            else:
                L.pop(0)
                idx.pop(0)
        else:
            L.append(L.pop(0))
            idx.append(idx.pop(0))

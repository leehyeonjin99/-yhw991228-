import sys, math
N, M=map(int, sys.stdin.readline().split())
L=list(map(int, sys.stdin.readline().split()))
print(L)
count=0
for _ in range(M):
    if L[0]==1:
        L.pop(0)
        for i in range(len(L)):
            L[i]=L[i]-1
        N=N-1
    else:
        if N-L[0]+1<L[0]-1:
            count+=N-L[0]+1
            for i in range(1, len(L)):
                if L[i]+(N-L[0]+1)>N:
                    L[i]=(L[i]+(N-L[0]+1))%N-1
                else:
                    L[i]=L[i]+(N-L[0]+1)-1
        else:
            count+=L[0]-1
            for i in range(1, len(L)):
                L[i]-=L[0]-1
                if L[i]<1:
                    L[i]+=N
                L[i]-=1
        L.pop(0)
        N=N-1

print(count)

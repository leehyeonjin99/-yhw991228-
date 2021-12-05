import sys
N=int(sys.stdin.readline())
L=[0 for _ in range(1000000)]
L[0],L[1]=1,2
for i in range(2, N):
    L[i]=(L[i-1]+L[i-2])%15746
print(L[N-1])
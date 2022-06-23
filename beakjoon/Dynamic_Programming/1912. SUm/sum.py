import sys
N=int(sys.stdin.readline())
L=list(map(int, sys.stdin.readline().split()))
R=L.copy()

for i in range(1,N):
    R[i]=max(R[i],L[i]+R[i-1])

print(max(R))
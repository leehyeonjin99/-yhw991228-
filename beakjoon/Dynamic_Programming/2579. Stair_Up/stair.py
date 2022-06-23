import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline()))
cost=L.copy()

if N>1:
    cost[1]=L[0]+L[1]
if N>2:
    cost[2]=max(L[1]+L[2],L[0]+L[2])
for i in range(3,N):
    cost[i]=max(L[i]+cost[i-2], L[i]+L[i-1]+cost[i-3])

print(cost[-1])
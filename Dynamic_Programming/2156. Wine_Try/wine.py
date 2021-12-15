import sys
N=int(sys.stdin.readline())
wine=[]
for i in range(N):
    wine.append(int(sys.stdin.readline()))

total=[0 for _ in range(N)]
total[0]=wine[0]

if N>1:
    total[1]=wine[0]+wine[1]

if N>2:
    total[2]=max(wine[0]+wine[2], wine[1]+wine[2], total[1])

for i in range(3, N):
    total[i]=max(total[i-1], total[i-3]+wine[i-1]+wine[i], total[i-2]+wine[i])

print(total[-1])
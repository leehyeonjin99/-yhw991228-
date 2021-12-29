import sys
N=int(sys.stdin.readline())
D=list(map(int, sys.stdin.readline().split()))
P=list(map(int, sys.stdin.readline().split()))

m=P[0]
sum=0
for i,dist in enumerate(D):
    sum+=m*dist
    if P[i+1]<m:
        m=P[i+1]
print(sum)
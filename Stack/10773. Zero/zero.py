import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    n=int(sys.stdin.readline())
    if n==0:
        L.pop()
    else:
        L.append(n)
print(sum(L))
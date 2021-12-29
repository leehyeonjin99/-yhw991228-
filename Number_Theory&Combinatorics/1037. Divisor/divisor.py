import sys
N=int(sys.stdin.readline())
L=list(map(int, sys.stdin.readline().split()))
L.sort()
if len(L)%2==0:
    result=L[0]*L[-1]
else:
    result=L[len(L)//2]**2
print(result)
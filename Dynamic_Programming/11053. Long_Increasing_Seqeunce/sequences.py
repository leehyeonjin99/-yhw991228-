import sys
N=int(sys.stdin.readline())
L=list(map(int, sys.stdin.readline().split()))

length=[1 for _ in range(N)]
for i in range(1,N):
    M=length[i]
    for j in range(i):
        if L[j]<L[i]:
            if (length[j]+1)>M:
                M=length[j]+1
    length[i]=M
print(max(length))
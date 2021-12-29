import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
L.sort(key=lambda x : x[0])
second=[x[1] for x in L]
Long=[1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if second[j]<second[i]:
            Long[i]=max(Long[i],Long[j]+1)
print(N-max(Long))
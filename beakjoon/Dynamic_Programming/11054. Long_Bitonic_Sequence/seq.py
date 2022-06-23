import sys
N=int(sys.stdin.readline())
L=list(map(int, sys.stdin.readline().split()))
L_rev=L[::-1]
increase=[1 for _ in range(N)]
decrease=[1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if L[j]<L[i]:
            increase[i]=max(increase[i],increase[j]+1)
        if L_rev[j]<L_rev[i]:
            decrease[i]=max(decrease[i],decrease[j]+1)

decrease=decrease[::-1]
total=[]
for i in range(N):
    total.append(increase[i]+decrease[i])
print(max(total)-1)

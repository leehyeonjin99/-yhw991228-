import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
'''
sum=0
for num in range(N):
    temp=L[num].copy()
    temp.remove(L[num][color])
    sum+=min(temp)
    if color==L[num].index(min(temp)):
        color=temp.index(min(temp))+1
    else:
        color=L[num].index(min(temp))
'''
for i in range(1,N):
    L[i][0]+=min(L[i-1][1],L[i-1][2])
    L[i][1]+=min(L[i-1][0],L[i-1][2])
    L[i][2]+=min(L[i-1][1],L[i-1][0])
print(min(L[N-1]))

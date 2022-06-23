import sys
N=int(sys.stdin.readline())
solution=[0 for i in range(N)]
if N>1:
    solution[1]=1
if N>2:
    solution[2]=1
for i in range(3,N):
    solution[i]=solution[i-1]+1
    if (i+1)%2==0:
        solution[i]=min(solution[i],solution[i//2]+1)
    if (i+1)%3==0:
        solution[i]=min(solution[i],solution[i//3]+1)
print(solution[-1])


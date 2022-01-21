import sys
N=int(sys.stdin.readline())
que=[i for i in range(1,N+1)]
idx=0
while len(que)-idx!=1:
    if idx%2==1:
        que.append(que[idx])
    idx+=1
print(que[idx])

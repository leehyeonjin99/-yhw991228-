import sys
N=int(sys.stdin.readline())
que=[]
idx=0
for i in range(N):
    problem=list(sys.stdin.readline().split())
    order=problem[0]
    if order=='push':
        que.append(int(problem[1]))
    elif order=='pop':
        if len(que)-idx<=0:
            print(-1)
        else:
            print(que[idx])
            idx+=1
    elif order=='size':
        print(len(que)-idx)
    elif order=='empty':
        if len(que)-idx<=0:
            print(1)
        else:
            print(0)
    elif order=='front':
        if len(que)-idx<=0:
            print(-1)
        else:
            print(que[idx])
    elif order=='back':
        if len(que)-idx<=0:
            print(-1)
        else:
            print(que[-1])
    

    
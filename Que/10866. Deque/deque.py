import sys
N=int(sys.stdin.readline())
deque=[]
for _ in range(N):
    L=list(sys.stdin.readline().split())
    order=L[0]
    if order=='push_front':
        deque=[int(L[1])]+deque
    elif order=='push_back':
        deque.append(int(L[1]))
    elif order=='pop_front':
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop(0))
    elif order=='pop_back':
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop())
    elif order=='size':
        print(len(deque))
    elif order=='empty':
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif order=='front':
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif order=='back':
        if len(deque)==0:
            print(-1)
        else:
            print(deque[-1])

import sys
N,K=map(int, sys.stdin.readline().split())
L=[i+1 for i in range(N)]
R=[]
idx=0
for i in range(N):
    idx+=K-1
    if idx>=len(L):
        idx=idx%len(L)
    R.append(L.pop(idx))
print('<', end='')
for i, r in enumerate(R):
    if i<len(R)-1:
        print(r, end=', ')
    else:
        print(f"{r}>")
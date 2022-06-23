import sys
N=int(sys.stdin.readline())
L=list(map(int,sys.stdin.readline().split()))
'''
for i in range(N):
    R=[-1]
    for j in L[i+1:]:
        if j>L[i]:
            R.append(j)
            break
    if len(R)==1:
        print(R[0],end=' ')
    else:
        print(R[1],end=' ')
'''
stack=[]
for i in range(N):
    while stack and L[stack[-1]]<L[i]:
        L[stack[-1]]=L[i]
        stack.pop()
    stack.append(i)

print(stack)

while stack:
    L[stack[-1]]=-1
    stack.pop()

for i in L:
    print(i, end=' ')
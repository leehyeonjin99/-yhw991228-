import sys
N=int(sys.stdin.readline())
L=[]

def push(stack, X):
    stack.append(X)
def size(stack):
    print(len(stack))
def empty(stack):
    if len(stack)==0:
        print(1)
    else:
        print(0)
def top(stack):
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])
def POP(stack):
    if len(stack)==0:
        print(-1)
    else:
        print(stack.pop())

for i in range(N):
    command=list(sys.stdin.readline().split())
    if command[0]=='push':
        push(L,int(command[1]))
    elif command[0]=='pop':
        POP(L)
    elif command[0]=='size':
        size(L)
    elif command[0]=='empty':
        empty(L)
    elif command[0]=='top':
        top(L)
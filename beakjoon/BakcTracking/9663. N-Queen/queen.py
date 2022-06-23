import sys
N=int(sys.stdin.readline())
board=[-1 for _ in range(N)]

'''
import itertools
perm=itertools.permutations(range(N),N)

def check_queen(array, N):
    check=True
    L=[]
    for n, num in enumerate(array):
        L.append([n,num])
    for i in range(N):
        for j in range(i+1,N):
            if abs(L[i][0]-L[j][0])==abs(L[i][1]-L[j][1]):
                return False
    return True
'''
def check(i):
    for j in range(i):
        if (board[j]==board[i]) or (abs(board[i]-board[j])==i-j):
            return False
    return True

count=0
visited=[False for _ in range(N)]
def queen(x):
    global count

    if x==N:
        count+=1
        return

    for i in range(N):
        if visited[i]:
            continue
        board[x]=i
        if check(x):
            visited[i]=True
            queen(x+1)
            visited[i]=False

queen(0)
print(count)
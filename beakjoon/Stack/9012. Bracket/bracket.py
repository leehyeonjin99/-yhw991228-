import sys
N=int(sys.stdin.readline())
for i in range(N):
    L=list(sys.stdin.readline())
    L=L[:-1]
    C=[]
    check=True
    for l in L:
        if l=='(':
            C.append(1)
        elif l==')':
            if len(C)==0:
                check=False
                break
            else:
                C.pop()
    if check:
        if len(C)==0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
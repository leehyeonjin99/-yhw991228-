import sys

while(1):
    L=list(sys.stdin.readline())
    L=L[:-1]
    if L[0]=='.':
        break
    C=[]
    check=True
    for l in L:
        if l=='(':
            C.append(0)
        elif l=='[':
            C.append(1)
        elif l==')':
            if (len(C)==0) or (C[-1]==1):
                check=False
                break
            else:
                C.pop()
        elif l==']':
            if (len(C)==0) or (C[-1]==0):
                check=False
                break
            else:
                C.pop()
    if check:
        if len(C)==0:
            print('yes')
        else:
            print('no')
    else:
        print('no')

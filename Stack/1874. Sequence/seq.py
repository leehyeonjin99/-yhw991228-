import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline()))
R=[]
C=[]
Cal=[]
check=0
for i in range(1,N+1):
    R.append(i)
    Cal.append('+')
    while(R[-1]==L[check]):
        C.append(R.pop())
        Cal.append('-')
        check+=1
        if (check>=N) or (len(R)==0):
            break
if C==L:
    for c in Cal:
        print(c)
else:
    print('NO')

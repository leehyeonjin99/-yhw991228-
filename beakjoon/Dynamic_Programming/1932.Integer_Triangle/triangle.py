import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
S=[L[0]]
for row in range(1, N):
    s=[]
    if row==1:
        for num in L[row]:
            s.append(num+L[row-1][0])
    else:
        for col, num in enumerate(L[row]):
            if col==0:
                s.append(num+S[row-1][col])
            elif col<len(L[row])-1:
                s.append(num+max(S[row-1][col-1], S[row-1][col]))
            else:
                s.append(num+S[row-1][col-1])
    S.append(s)
    
print(max(S[N-1]))
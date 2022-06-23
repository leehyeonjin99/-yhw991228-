import sys
A=sys.stdin.readline().rstrip()
B=sys.stdin.readline().rstrip()
L=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1]==B[j-1]:
            L[i][j]=L[i-1][j-1]+1
        else:
            L[i][j]=max(L[i-1][j], L[i][j-1])

print(L[-1][-1])


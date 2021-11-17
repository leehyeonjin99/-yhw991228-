import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(list(map(int,sys.stdin.readline().split(' '))))

'''for i in range(N-1):
    for j in range(N-1):
        if (L[j][0]>L[j+1][0])|((L[j][0]==L[j+1][0])and(L[j][1]>L[j+1][1])):
            temp=L[j]
            L[j]=L[j+1]
            L[j+1]=temp'''

L.sort(key=lambda x : (x[0],x[1]))

for i in range(N):
    for num in L[i]:
        print(num, end=' ')
    print()
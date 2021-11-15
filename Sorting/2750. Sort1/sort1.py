N=int(input())
L=[]
for i in range(N):
    L.append(int(input()))

# L.sort()
for i in range(N-1):
    for j in range(N-1):
        if L[j]>L[j+1]:
            temp=L[j]
            L[j]=L[j+1]
            L[j+1]=temp
for i in L:
    print(i)
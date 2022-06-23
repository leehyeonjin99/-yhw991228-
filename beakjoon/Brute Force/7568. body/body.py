N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
rank_list=[]
for i in range(N):
    count=0
    for j in range(N):
        if (L[i][0]<L[j][0])&(L[i][1]<L[j][1]):
            count+=1
    rank_list.append(count+1)
for i in rank_list:
    print(i, end=" ")
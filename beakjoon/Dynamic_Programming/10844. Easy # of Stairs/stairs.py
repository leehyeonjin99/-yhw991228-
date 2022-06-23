import sys
N=int(sys.stdin.readline())
next_num=[1,2,2,2,2,2,2,2,2,1]
num=[0 for _ in range(10)]
for i in range(N):
    temp=[0 for _ in range(10)]
    for j in range(10):
        if i==0 and j!=0:
            temp[j]+=1
        else:
            if j==0:
                temp[j+1]+=num[j]
            elif j==9:
                temp[j-1]+=num[j]
            else:
                temp[j-1]+=num[j]
                temp[j+1]+=num[j]
    num=temp
print(sum(num)%1000000000)
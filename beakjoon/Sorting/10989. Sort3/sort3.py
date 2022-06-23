import sys

N=int(input())
count_arr=[0]*10001

for i in range(N):
    count_arr[int(sys.stdin.readline())]+=1

for i in range(len(count_arr)):
    while count_arr[i]:
        print(i)
        count_arr[i]-=1
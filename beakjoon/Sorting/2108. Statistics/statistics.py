from collections import Counter
import sys

N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline()))
'''
def mode(arr):
    count_list=[0]*(max(arr)-min(arr)+1)

    for num in arr:
        count_list[num-min(arr)]+=1

    max_list=[]
    for i in range(len(count_list)):
        if max(count_list)==count_list[i]:
            max_list.append(i)

    for i in range(len(max_list)):
        max_list[i]+=min(arr)
    
    if len(max_list)==1:
        return max_list[0]
    else:
        return max_list[1]
'''
print(round(sum(L)/N))

L.sort()
print(L[N//2])

cnt=Counter(L).most_common()
if (len(cnt)>1) & (cnt[0][1]==cnt[1][1]):
        print(cnt[1][0])
else:
    print(cnt[0][0])

#print(mode(L))
print(max(L)-min(L))

def merge_sort(L):
    if len(L)<=1:
        return L
    
    mid=len(L)//2
    left=merge_sort(L[:mid])
    right=merge_sort(L[mid:])

    i,j,k=0,0,0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            L[k]=left[i]
            i+=1
        else:
            L[k]=right[j]
            j+=1
        k+=1
    
    if i==len(left):
        while j<len(right):
            L[k]=right[j]
            j+=1
            k+=1
    elif j==len(right):
        while i<len(left):
            L[k]=left[i]
            i+=1
            k+=1
    return L

import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline()))
L=merge_sort(L)
for num in L:
    print(num)


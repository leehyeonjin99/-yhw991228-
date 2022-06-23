import sys

def cal(n, num, idx, add , sub, multi, division):
    global maxv, minv
    if idx==n:
        maxv=max(num, maxv)
        minv=min(num, minv)
        return
    else:
        if add :
            cal(N, num+num_list[idx], idx+1, add-1, sub, multi, division)
        if sub :
            cal(N, num-num_list[idx], idx+1, add, sub-1, multi, division)
        if multi :
            cal(N, num*num_list[idx], idx+1, add, sub, multi-1, division)
        if division :
            cal(N, -(-num//num_list[idx]) if num<0 else num//num_list[idx], idx+1, add, sub, multi, division-1)

maxv=-sys.maxsize-1
minv=sys.maxsize
N=int(sys.stdin.readline())
num_list=list(map(int, sys.stdin.readline().split()))
a, b, c, d=map(int,sys.stdin.readline().split())
cal(N, num_list[0], 1, a, b, c, d)
print(maxv)
print(minv)
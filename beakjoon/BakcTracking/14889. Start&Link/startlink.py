import sys
import itertools

N=int(sys.stdin.readline())
L=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
all=range(N)
start_list=list(itertools.combinations(range(N), N//2))

min_num=sys.maxsize

for start in start_list:
    start_two=list(itertools.combinations(start, 2))
    start_sum=0
    for t in start_two:
        start_sum+=(L[t[0]][t[1]]+L[t[1]][t[0]])
        
    link=[mem for mem in all if mem not in list(start)]
    link_two=list(itertools.combinations(link, 2))
    link_sum=0
    for t in link_two:
        link_sum+=(L[t[0]][t[1]]+L[t[1]][t[0]])
    sub=abs(start_sum-link_sum)
    if sub<min_num:
        min_num=sub

print(min_num)
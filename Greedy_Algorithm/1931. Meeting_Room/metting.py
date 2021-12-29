import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(list(map(int,sys.stdin.readline().split())))
L.sort(key=lambda x : (x[1],x[0]))

end=L[0][1]
count=1
for l in L[1:]:
    if l[0]>=end:
        count+=1
        end=l[1]
        continue

print(count)


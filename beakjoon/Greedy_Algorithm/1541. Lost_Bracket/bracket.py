import sys
L=list(sys.stdin.readline()[:-1].split('-'))

for i,l in enumerate(L):
    A=list(map(int, l.split('+')))
    sum=0
    for a in A:
        sum+=a
    L[i]=sum

sum=L[0]
for l in L[1:]:
    sum=sum-l

print(sum)
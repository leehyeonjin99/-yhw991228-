import sys
import math
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline()))
L.sort()
S=[]
for i in range(N-1):
    S.append(L[i+1]-L[i])
GCD=S[0]
if N>2:
    for s in S[1:]:
        GCD=math.gcd(GCD,s)
R=[]
for i in range(2,int(math.sqrt(GCD)+1)):
    if GCD%i==0:
        R.append(i)
        if i!=int(GCD//i):
            R.append(int(GCD//i))
R.sort()
for i in R:
    print(i, end=' ')
print(GCD)
'''
num=2
result=[]
while 1:
    if num>=max(L):
        break
    remainder=L[0]%num
    for l in L[1:]:
        if l%num!=remainder:
            break
    if (l==L[-1]) & (l%num==remainder):
        result.append(num)
    if num>=min(L):
        num+=min(L)
    else:
        num+=1
for i in result:
    print(i, end=' ')
'''
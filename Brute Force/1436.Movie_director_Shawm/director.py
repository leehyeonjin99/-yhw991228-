def triple_six(N):
    count=0
    check=False
    while N!=0:
        if N%10==6:
            if (count==0)|(check==True):
                count+=1
                check=True
                if count==3:
                    return True
        else:
            check=False
            count=0
        N=N//10
    return False

N=int(input())
num=665
count=0

while count!=N:
    num+=1
    if triple_six(num):
        count+=1

print(num)

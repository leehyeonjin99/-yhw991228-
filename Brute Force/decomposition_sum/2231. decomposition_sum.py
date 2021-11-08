N=int(input())
N_copy=N
length=0
while N_copy!=0:
    N_copy=N_copy//10
    length+=1

check=False
if N-length*9>0:
    decomp_number=N-length*9
else:
    decomp_number=0
while check==False:
    temp=sum=decomp_number
    while(temp!=0):
        sum+=temp%10
        temp=temp//10
    if sum==N:
        check=True
    else:
        if decomp_number+1>N:
            break
        else:
             decomp_number+=1
    


if check==True:
    print(decomp_number)
else:
    print(0)




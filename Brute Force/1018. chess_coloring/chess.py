N,M=map(int,input().split())
board=[]

for i in range(N):
    row=input()
    temp=[]
    for color in row:
        temp.append(color)
    board.append(temp)


min_count=64
min_i=0
min_j=0
for i in range(N-7):
    for j in range(M-7):
        W_count=0
        B_count=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if board[a][b]!='W':
                        W_count+=1
                    if board[a][b]!='B':
                        B_count+=1
                if (a+b)%2==1:
                    if board[a][b]!='W':
                        B_count+=1
                    if board[a][b]!='B':
                        W_count+=1
        if min(W_count, B_count)<min_count:
            min_count=min(W_count, B_count)
            min_i, min_j=i, j

print(min_count)
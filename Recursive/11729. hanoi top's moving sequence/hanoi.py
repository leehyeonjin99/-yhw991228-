def hanoi_count(n):
    if n==1:
        return 1
    else:
        return 2*hanoi_count(n-1)+1

def hanoi(n,a,c,b):
    if n==1:
        print(a, c)
    else:
        hanoi(n-1,a,b,c)
        print(a, c)
        hanoi(n-1,b,c,a)

n=int(input())
print(hanoi_count(n))
hanoi(n,1,3,2)

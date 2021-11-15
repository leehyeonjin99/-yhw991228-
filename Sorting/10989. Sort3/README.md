[10989](https://www.acmicpc.net/problem/10989)

## 문제
> N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
## 입력
> 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
## 출력
> 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

## 해결방안
> Counting Sort : O(N+K)
> 원소들간의 비교를 하지 않는 정렬 알고리즘
> 
> 조건1. 리스트 내의 모든 원소들은 0~K의 범위를 가져야만 한다. 즉 음수나 소수가 있으면 사용불가
> 
> 조건2. K=O(N)으로 나타낼 수 있어야만 한다.

![image](https://user-images.githubusercontent.com/57162812/141814544-a2973cd5-273f-4b8c-b497-c53a2f95247d.png)

```python

MAX_NUM=1000000

def counting_sort(arr):
    count_arr=[0]*(MAX_NUM+1)
    count_sum=[0]*(MAX_NUM+1)
    length=len(arr)
    
    for i in range(length):
        count_arr[arr[i]]+=1
    
    count_sum[0]=count_arr[0]
    for i in range(1, MAX_NUM+1):
        count_sum[i]=count_sum[i-1]+count_arr[i]
    
    sorted_arr=[0]*(length+1)
    for i in range(length-1,-1,-1):
        sorted_arr[count_sum[arr[i]]]=arr[i]
        count_sum[arr[i]]-=1
    return sorted_arr[1:]
```

>메모리 초과 오류가 발생하였다.
>
>따라서 count sum는 생략하고 count된 수만큼 출력해주는 방식으로 해결하였다.

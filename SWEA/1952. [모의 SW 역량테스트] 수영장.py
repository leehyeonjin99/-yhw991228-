from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    one_day, one_month, three_month, one_year = map(int, input().split())
    year_schedule = list(map(int, input().split()))
    min_result = one_year
    que = deque([[0, 0]])
    while que:
        now_month, now_cost = que.popleft()
        if now_month > 11:
            min_result = min(min_result, now_cost)
            continue
        elif now_cost >= min_result:
            continue

        # 하루
        que.append([now_month + 1, now_cost + year_schedule[now_month] * one_day])
        # 한달
        que.append([now_month + 1, now_cost + one_month])
        # 석달
        que.append([now_month + 3, now_cost + three_month])
        
    print(f"#{test_case}",min_result)
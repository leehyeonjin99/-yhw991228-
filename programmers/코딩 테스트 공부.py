from collections import deque
import sys

def solution(alp, cop, problems):
    answer = sys.maxsize
    max_alp = 0
    max_cop = 0
    
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    
    que = deque([])
    que.append([0, alp, cop])
    while(que):
        print("=" * 10)
        now_cost, now_alp, now_cop = que.popleft()
        print("Now : ", now_cost, now_alp, now_cop)
        if now_alp >= max_alp and now_cop >= max_cop:
            answer = min(now_cost, answer)
            continue
        # alp를 공부로 채움
        if now_alp < max_alp:
            que.append([now_cost + 1, now_alp + 1, now_cop])
            print("ALP :", now_cost + 1, now_alp + 1, now_cop)
        # cop를 공부로 채움
        if now_cop < max_cop:
            que.append([now_cost + 1, now_alp, now_cop + 1])
            print("COP :", now_cost + 1, now_alp, now_cop + 1)
        # alp, cop를 문제풀이로 채움
        for (alp_req, cop_req, alp_rwd, cop_rwd, cost) in problems:
            if now_alp < alp_req or now_cop < cop_req:
                continue
            next_alp = now_alp + alp_rwd
            next_cop = now_cop + cop_rwd
            next_cost = now_cost + cost
            que.append([next_cost, next_alp, next_cop])
            print("SOLV :", next_cost, next_alp, next_cop)
    
    return answer

solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])
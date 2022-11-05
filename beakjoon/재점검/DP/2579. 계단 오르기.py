import sys
from collections import deque

N = int(sys.stdin.readline())
scores = []
for _ in range(N):
    scores.append(int(sys.stdin.readline()))

# bfs : 메모리 초과
# answer = 0
# que = deque([[0, 0, 0]]) # 현재 위치, 현재 점수, 연달아 밟은 개수
# while que:
#     now_pos, now_score, now_cnt = que.popleft()
#     if now_pos == N:
#         answer = max(answer, now_score)
#         continue
#     if now_pos > N:
#         continue
#     if now_cnt < 2 and now_pos + 1 <= N:
#         que.append([now_pos + 1, now_score + scores[now_pos + 1], now_cnt + 1])
#     if now_pos + 2 <= N:
#         que.append([now_pos + 2, now_score + scores[now_pos + 2], 1])

# print(answer)

DP = [0 for _ in range(N)]
DP[0] = scores[0]
if N > 1:
    DP[1] = scores[0] + scores[1]
if N > 2:
    DP[2] = max(scores[0] + scores[2], scores[1] + scores[2])
for idx in range(3, N):
    DP[idx] = max(DP[idx - 2] + scores[idx], DP[idx - 3] + scores[idx - 1] + scores[idx])

print(DP[N - 1])
import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
power = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    power.append(tmp)

answer = sys.maxsize
team = set(range(N))
for team1 in combinations(team, N //2):
    team1_power = 0
    for (p1, p2) in combinations(team1, 2):
        team1_power += (power[p1][p2] + power[p2][p1])
    team2 = team - set(team1)
    team2_power = 0
    for (p1, p2) in combinations(team2, 2):
        team2_power += (power[p1][p2] + power[p2][p1])
    diff = abs(team1_power - team2_power)
    answer = min(answer, diff)

print(answer)
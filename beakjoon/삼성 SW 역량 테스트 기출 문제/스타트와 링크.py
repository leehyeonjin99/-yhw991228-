import sys
from itertools import combinations

N = int(sys.stdin.readline())
ability = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    ability.append(tmp)
all_members = set(range(N))

diff_min = sys.maxsize
# print(diff_min)
for team in combinations(range(N), N//2):
    another_team = all_members - set(team)
    team_ability = 0
    another_team_ability = 0
    for two in combinations(team, 2):
        team_ability += (ability[two[0]][two[1]] + ability[two[1]][two[0]])
    for two in combinations(another_team, 2):
        another_team_ability += (ability[two[0]][two[1]] + ability[two[1]][two[0]])
    team_diff = abs(team_ability - another_team_ability)
    diff_min = min(diff_min, team_diff)

print(diff_min)    
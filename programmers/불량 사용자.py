import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    re_answer = 0
    for n_item in permutations(user_id, len(banned_id)):
        check = True
        for user, ban in zip(n_item, banned_id):
            ban = re.sub('\*', '.', ban)
            if len(ban) != len(user) or re.match(ban, user) == None:
                check = False
                break
        if check:
            n_item = sorted(list(n_item))
            if n_item not in answer:
                print(n_item)
                answer.append(n_item)
                re_answer += 1
    return re_answer

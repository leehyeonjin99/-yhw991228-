import itertools

N, M=map(int, input().split())
card=list(map(int,input().split()))
card_combination=list((itertools.combinations(card, 3)))
card_sum=[]

for cards in card_combination:
    if sum(cards)<=M:
        card_sum.append(sum(cards))

print(max(card_sum))

from itertools import combinations
card_total, target = map(int, input().split())
card_list = list(map(int, input().split()))
biggest_num =0
for cards in combinations(card_list, 3):
    temp_sum = sum(cards)
    if biggest_num < temp_sum <= target:
        biggest_num = temp_sum
print(biggest_num)
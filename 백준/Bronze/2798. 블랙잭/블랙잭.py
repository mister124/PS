import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
card_list = list(map(int, input().split()))
ans = 0
for com in combinations(card_list, 3):
    card_sum = sum(com)
    if card_sum <= M:
        ans = max(card_sum, ans)
        if ans == M:
            break
print(ans)

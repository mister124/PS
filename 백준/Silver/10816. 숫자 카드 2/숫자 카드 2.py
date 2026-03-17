import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
case = list(map(int, input().split()))
M = int(input())
answer = list(map(int, input().split()))
data = dict(Counter(case))
for key in answer:
    print(data.get(key, 0), end=" ")
import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
jewels.sort()
bags = [int(input()) for _ in range(K)]
bags.sort()

total = 0
capable_jewels = []
j_idx = 0
for bag in bags:
    while j_idx < N and jewels[j_idx][0] <= bag:
        heapq.heappush(capable_jewels, -jewels[j_idx][1])
        j_idx += 1

    if capable_jewels:
        total += -heapq.heappop(capable_jewels)

print(total)

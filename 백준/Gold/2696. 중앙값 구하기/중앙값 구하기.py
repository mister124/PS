import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    nums = []
    for _ in range((M - 1) // 10 + 1):
        nums.extend(list(map(int, input().split())))
    left_heap = []
    right_heap = []
    ans = []
    for i, num in enumerate(nums):
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -num)
        else:
            heapq.heappush(right_heap, num)
        if right_heap and -left_heap[0] > right_heap[0]:
            left_val = -heapq.heappop(left_heap)
            right_val = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -right_val)
            heapq.heappush(right_heap, left_val)
        if i % 2 == 0:
            ans.append(-left_heap[0])
    print(len(ans))
    for i in range(0, len(ans), 10):
        print(*(ans[i : i + 10]))
